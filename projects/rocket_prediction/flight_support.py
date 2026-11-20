"""Provided bookkeeping for the guided flight model; student physics stays in the notebook."""

from dataclasses import dataclass
from pathlib import Path
import numpy as np


@dataclass(frozen=True)
class FlightInputs:
    mass_kg: float
    density_kg_m3: float
    body_cd: float
    body_area_m2: float
    parachute_cd: float
    parachute_area_m2: float
    ejection_delay_s: float
    gravity_m_s2: float = 9.81

    def validate(self):
        for name in ("mass_kg", "density_kg_m3", "body_area_m2",
                     "parachute_area_m2", "gravity_m_s2"):
            value = getattr(self, name)
            if not np.isfinite(value) or value <= 0:
                raise ValueError(f"{name} must be finite and positive.")
        for name in ("body_cd", "parachute_cd", "ejection_delay_s"):
            value = getattr(self, name)
            if not np.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and nonnegative.")


def load_motor(path):
    """Load the supplied, normalized D12 CSV. No downloads occur in the notebook."""
    data = np.genfromtxt(Path(path), delimiter=",", names=True)
    time = np.atleast_1d(data["time_s"])
    thrust = np.atleast_1d(data["thrust_N"])
    if (len(time) < 2 or not np.all(np.isfinite(time))
            or not np.all(np.isfinite(thrust)) or time[0] != 0
            or np.any(np.diff(time) <= 0) or np.any(thrust < 0)
            or thrust[0] != 0 or thrust[-1] != 0 or thrust.max() <= 0):
        raise ValueError("Motor data need increasing time from zero and nonnegative thrust with zero endpoints.")
    return time, thrust


def simulate(inputs, motor_time, motor_thrust, drag_force, advance_step,
             dt_s=0.01, max_time_s=180.0):
    """Integrate using student drag and step functions; supplied event bookkeeping.

    Positive direction is upward. Thrust is piecewise linear, averaged over
    each interval. Steps split at motor knots and the fixed deployment time.
    Recovery deployment is modeled as an instantaneous change in Cd*A.
    The final touchdown time/velocity are linearly interpolated within a step.
    """
    inputs.validate()
    if not np.isfinite(dt_s) or dt_s <= 0 or not np.isfinite(max_time_s) or max_time_s <= 0:
        raise ValueError("dt_s and max_time_s must be finite and positive.")
    motor_time = np.asarray(motor_time, dtype=float)
    motor_thrust = np.asarray(motor_thrust, dtype=float)
    if (motor_time.ndim != 1 or motor_time.shape != motor_thrust.shape
            or motor_time.size < 2 or not np.all(np.isfinite(motor_time))
            or not np.all(np.isfinite(motor_thrust)) or motor_time[0] != 0
            or np.any(np.diff(motor_time) <= 0) or np.any(motor_thrust < 0)
            or motor_thrust[0] != 0 or motor_thrust[-1] != 0
            or motor_thrust.max() <= 0):
        raise ValueError("Invalid motor time/thrust arrays.")
    burnout_s = float(motor_time[-1])
    deployment_s = burnout_s + inputs.ejection_delay_s
    # Columns: time, acceleration, velocity, height. Initial acceleration is
    # constrained by the pad, so it is zero rather than -g.
    rows = [[0.0, 0.0, 0.0, 0.0]]
    phases = ["on pad"]
    t, h, v = 0.0, 0.0, 0.0
    launched = False
    while t < max_time_s - 1e-12:
        future_knots = motor_time[motor_time > t + 1e-10]
        next_knot = float(future_knots[0]) if future_knots.size else max_time_s
        next_event = deployment_s if deployment_s > t + 1e-10 else max_time_s
        step_dt = min(dt_s, next_knot - t, next_event - t, max_time_s - t)
        next_t = t + step_dt
        thrust_start = np.interp(t, motor_time, motor_thrust, right=0.0)
        thrust_end = np.interp(next_t, motor_time, motor_thrust, right=0.0)
        average_thrust = float((thrust_start + thrust_end) / 2)
        under_parachute = t >= deployment_s - 1e-10
        cd = inputs.parachute_cd if under_parachute else inputs.body_cd
        area = inputs.parachute_area_m2 if under_parachute else inputs.body_area_m2
        drag = drag_force(inputs.density_kg_m3, v, cd, area)
        next_h, next_v, acceleration = advance_step(
            h, v, average_thrust, drag, inputs.mass_kg,
            inputs.gravity_m_s2, step_dt)
        if not np.all(np.isfinite([next_h, next_v, acceleration])):
            raise ValueError("Nonfinite trajectory: check your equations, inputs, and time step.")
        phase = "parachute" if under_parachute else ("powered" if t < burnout_s - 1e-10 else "coast")
        if not launched and next_v <= 0:
            next_h, next_v, acceleration, phase = 0.0, 0.0, 0.0, "on pad"
            if next_t >= burnout_s - 1e-10:
                raise RuntimeError("No liftoff. Check mass, thrust, signs, and the constant-mass approximation.")
        else:
            launched = True
        if launched and next_h <= 0 and next_v < 0:
            fraction = h / (h - next_h)
            next_t = t + fraction * step_dt
            next_v = v + fraction * (next_v - v)
            rows.append([next_t, acceleration, next_v, 0.0])
            phases.append("touchdown")
            break
        rows.append([next_t, acceleration, next_v, next_h])
        phases.append(phase)
        t, h, v = next_t, next_h, next_v
    else:
        raise RuntimeError("No touchdown before max_time_s. Check equations, step size, and recovery inputs.")
    values = np.asarray(rows, dtype=float)
    return dict(time_s=values[:, 0], acceleration_m_s2=values[:, 1],
                velocity_m_s=values[:, 2], altitude_m=values[:, 3],
                phase=np.asarray(phases), burnout_s=burnout_s,
                deployment_s=deployment_s)


def summary(flight):
    peak = int(np.argmax(flight["altitude_m"]))
    return {
        "apogee_m": float(flight["altitude_m"][peak]),
        "time_to_apogee_s": float(flight["time_s"][peak]),
        "maximum_upward_speed_m_s": float(np.max(flight["velocity_m_s"])),
        "flight_time_s": float(flight["time_s"][-1]),
        "touchdown_velocity_m_s": float(flight["velocity_m_s"][-1]),
    }
