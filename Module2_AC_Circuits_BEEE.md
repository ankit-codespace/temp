# Module 2 — AC Circuits
### Basic Electrical & Electronics Engineering | UEC101T

---

## 1. What is Alternating Current?

DC (Direct Current) flows in one fixed direction. AC (Alternating Current) reverses direction periodically — it keeps swinging back and forth in a sinusoidal pattern.

The standard mathematical form of an AC voltage is:

**v(t) = V_m sin(ωt + φ)**

Where:
- **V_m** = Peak (maximum) voltage
- **ω** = Angular frequency = 2πf (rad/s)
- **f** = Frequency in Hz
- **φ** = Phase angle (initial phase shift)

---

## 2. Key AC Terms

| Term | Symbol | Meaning | Formula |
|------|--------|---------|---------|
| Frequency | f | Number of complete cycles per second | f = 1/T |
| Time Period | T | Time for one complete cycle | T = 1/f |
| Angular Frequency | ω | Rate of change of angle in radians | ω = 2πf |
| Peak Value | V_m / I_m | Maximum value in either direction | — |
| Phase | φ | Starting angle of the waveform at t = 0 | — |
| Phase Difference | θ | Angle by which one quantity leads/lags another | — |

In India, the supply is **50 Hz**, so T = 20 ms and ω = 314 rad/s.

---

## 3. RMS Value

**What it is:** The DC equivalent of an AC quantity — the value of DC that would produce the same heating effect as the AC in the same resistance.

Think of it this way: AC voltage is always changing, so you can't just use the peak value for power calculations. RMS gives you the "effective" value.

**Formula:**

$$V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 \times V_m$$

$$I_{rms} = \frac{I_m}{\sqrt{2}} \approx 0.707 \times I_m$$

> **Exam point:** The 230 V of your home supply is the RMS value, not the peak. The actual peak is 230 × √2 ≈ 325 V.

---

## 4. Average Value

The average of a full AC cycle is **zero** (positive and negative halves cancel). So average value is calculated over a **half cycle** only.

$$V_{avg} = \frac{2V_m}{\pi} \approx 0.637 \times V_m$$

---

## 5. Form Factor and Peak Factor

These are ratios used to describe the shape of a waveform.

**Form Factor** = RMS / Average = 0.707 / 0.637 = **1.11**

**Peak Factor (Crest Factor)** = Peak / RMS = V_m / (V_m/√2) = **√2 ≈ 1.414**

> These values (1.11 and 1.414) are standard for a pure sinusoidal waveform. If the waveform changes shape, these values change too.

---

## 6. Phasor Representation

AC quantities like voltage and current vary sinusoidally with time. Representing them on a time graph is messy when multiple quantities are involved.

A **phasor** is a rotating vector that represents the magnitude and phase of a sinusoidal quantity. You freeze the rotation at t = 0 and draw it as an arrow.

**Why it's useful:**
- Instead of writing v = V_m sin(ωt + 30°), you draw a vector of length V_m at 30°
- Adding two AC voltages becomes vector addition instead of trigonometric addition

**Key rule:**
- A quantity that **leads** another is drawn at a **higher angle** (anti-clockwise)
- A quantity that **lags** is drawn at a **lower angle** (clockwise)

---

## 7. Pure Resistive Circuit (R only)

When only resistance is in the circuit:
- Voltage and current are **in phase** (φ = 0°)
- No energy storage — all energy is consumed as heat

**Impedance:** Z = R

**Phasor diagram:** V and I point in the same direction.

---

## 8. Pure Inductive Circuit (L only)

An inductor opposes change in current. When AC flows through it:
- Current **lags** voltage by **90°**
- The opposition offered by an inductor is called **Inductive Reactance**

$$X_L = \omega L = 2\pi f L \quad (\Omega)$$

Higher the frequency, higher the opposition (inductor blocks high-frequency AC more).

**Impedance:** Z = X_L = jωL

**Memory tip:** *ELI* — In an inductive (L) circuit, E (voltage) comes before I (current) → current lags voltage.

---

## 9. Pure Capacitive Circuit (C only)

A capacitor opposes change in voltage. When AC flows through it:
- Current **leads** voltage by **90°**
- The opposition offered is called **Capacitive Reactance**

$$X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} \quad (\Omega)$$

Higher the frequency, lower the opposition (capacitor passes high-frequency AC easily).

**Memory tip:** *ICE* — In a capacitive (C) circuit, I (current) comes before E (voltage) → current leads voltage.

---

## 10. RL Series Circuit ⭐ (Tier 2 — Exam Priority)

A resistor and inductor connected in series with an AC supply.

### What happens:
- R consumes energy; L stores and returns it
- Current lags behind voltage by some angle φ (between 0° and 90°)

### Impedance Triangle

The voltage across R (V_R) and voltage across L (V_L) are at 90° to each other. So the total voltage V is their **vector sum**:

$$V = \sqrt{V_R^2 + V_L^2}$$

$$Z = \sqrt{R^2 + X_L^2} \quad (\Omega)$$

### Phase Angle

$$\tan\phi = \frac{X_L}{R} \quad \Rightarrow \quad \phi = \tan^{-1}\left(\frac{X_L}{R}\right)$$

Current lags voltage by angle φ.

### Key Formulas

| Quantity | Formula |
|----------|---------|
| Inductive Reactance | X_L = 2πfL |
| Impedance | Z = √(R² + X_L²) |
| Current | I = V/Z |
| Voltage across R | V_R = IR |
| Voltage across L | V_L = IX_L |
| Phase angle | φ = tan⁻¹(X_L / R) |
| Power Factor | cos φ = R/Z |

### Phasor Diagram (RL Series)

- Draw **I** horizontally (reference)
- Draw **V_R** in phase with I (horizontal)
- Draw **V_L** at 90° above V_R (since V leads I in inductor)
- Draw **V** as the diagonal (hypotenuse) from origin

> **Labels to include:** I (reference), V_R, V_L, V (resultant), angle φ

### Voltage Triangle

Same shape as impedance triangle — just multiply the impedance triangle by current I.

**Common mistake:** Students add V_R + V_L directly as numbers. They must be added as vectors (perpendicular). V ≠ V_R + V_L.

---

## 11. RC Series Circuit ⭐ (Tier 2 — Exam Priority)

A resistor and capacitor in series with AC supply.

### What happens:
- Current leads voltage by angle φ (between 0° and 90°)

### Impedance

$$Z = \sqrt{R^2 + X_C^2}$$

$$X_C = \frac{1}{2\pi f C}$$

### Phase Angle

$$\phi = \tan^{-1}\left(\frac{X_C}{R}\right)$$

Current **leads** voltage by φ.

### Key Formulas

| Quantity | Formula |
|----------|---------|
| Capacitive Reactance | X_C = 1/(2πfC) |
| Impedance | Z = √(R² + X_C²) |
| Current | I = V/Z |
| Voltage across R | V_R = IR |
| Voltage across C | V_C = IX_C |
| Phase angle | φ = tan⁻¹(X_C / R) |
| Power Factor | cos φ = R/Z |

### Phasor Diagram (RC Series)

- Draw **I** horizontally (reference)
- Draw **V_R** in phase with I (horizontal)
- Draw **V_C** at 90° **below** V_R (since V lags I in capacitor)
- Draw **V** as diagonal from origin going below horizontal

**Common mistake:** In RC, V_C is drawn below the reference — not above. Many students draw it above (that's RL).

---

## 12. RLC Series Circuit

Contains R, L, and C all in series. The inductive and capacitive reactances **oppose each other**.

$$X_{net} = X_L - X_C$$

$$Z = \sqrt{R^2 + (X_L - X_C)^2}$$

### Three possible conditions:

| Condition | Behaviour | Phase |
|-----------|-----------|-------|
| X_L > X_C | Circuit is inductive | Current lags voltage |
| X_C > X_L | Circuit is capacitive | Current leads voltage |
| X_L = X_C | **Resonance** | Current and voltage in phase, Z = R (minimum) |

### Resonance Frequency

At resonance, impedance is minimum and current is maximum:

$$f_r = \frac{1}{2\pi\sqrt{LC}}$$

---

## 13. Power in AC Circuits

In DC, power = VI. In AC, it's not that simple because voltage and current may be out of phase.

### Active Power (Real Power) — P

This is the actual power consumed (converted to heat, light, motion). Unit: **Watt (W)**

$$P = VI\cos\phi = I^2 R$$

### Reactive Power — Q

Power stored and returned by inductors and capacitors — it does no useful work. Unit: **VAR (Volt-Ampere Reactive)**

$$Q = VI\sin\phi = I^2 X$$

### Apparent Power — S

The total power supplied by the source. Unit: **VA (Volt-Ampere)**

$$S = VI = I^2 Z$$

### Relationship

$$S^2 = P^2 + Q^2$$

$$S = \sqrt{P^2 + Q^2}$$

---

## 14. Power Triangle ⭐ (Tier 2 — Exam Priority)

The three power quantities form a right triangle — called the **Power Triangle**.

```
        |S (Apparent Power)
        |         /
        |        /
      Q |       /
(Reactive)|    /
        |    /
        |  /
        | / φ
        |/____________
              P (Active Power)
```

- **Horizontal leg** = P (Active Power)
- **Vertical leg** = Q (Reactive Power)
- **Hypotenuse** = S (Apparent Power)
- **Angle φ** is the phase angle between V and I

### Power Factor

$$\cos\phi = \frac{P}{S} = \frac{R}{Z}$$

Power factor tells you how efficiently the circuit is using the supplied power.
- PF = 1 → purely resistive → all power is useful
- PF = 0 → purely reactive → no useful power consumed

> **Exam point:** For an RL circuit, the power factor is **lagging** (current lags voltage). For RC, it is **leading**.

### Diagram Labels (for exam)

Must include: P on horizontal, Q on vertical, S on hypotenuse, angle φ at origin, and the units (W, VAR, VA).

---

## 15. Quick Comparison — R, L, C in AC

| Property | Resistor (R) | Inductor (L) | Capacitor (C) |
|----------|-------------|--------------|---------------|
| Opposition | Resistance R | Reactance X_L = ωL | Reactance X_C = 1/ωC |
| Phase | V and I in phase | I lags V by 90° | I leads V by 90° |
| Power consumed | Yes (real power) | No (reactive) | No (reactive) |
| Effect of freq. | No change | X_L increases with f | X_C decreases with f |

---

## 16. Formula Reference — Module 2

```
RMS value:              V_rms = V_m / √2 = 0.707 × V_m
Average value:          V_avg = 0.637 × V_m
Form Factor:            K_f = 1.11  (for sine wave)
Peak Factor:            K_p = 1.414 (for sine wave)

Inductive reactance:    X_L = 2πfL                  (Ω)
Capacitive reactance:   X_C = 1 / (2πfC)            (Ω)

RL impedance:           Z = √(R² + X_L²)
RC impedance:           Z = √(R² + X_C²)
RLC impedance:          Z = √(R² + (X_L − X_C)²)

Phase angle (RL):       φ = tan⁻¹(X_L / R)         [lagging]
Phase angle (RC):       φ = tan⁻¹(X_C / R)         [leading]

Resonance frequency:    f_r = 1 / (2π√LC)

Active power:           P = VI cos φ = I²R           (W)
Reactive power:         Q = VI sin φ = I²X           (VAR)
Apparent power:         S = VI = I²Z                 (VA)
Power factor:           cos φ = P/S = R/Z
```

---

## 17. Common Exam Mistakes to Avoid

1. **Adding V_R and V_L directly** — they are at 90° to each other. Always use the Pythagorean theorem.

2. **Wrong phasor direction for C** — V_C is drawn *below* the reference (not above). V_L is above.

3. **Confusing X_L and X_C effect with frequency** — X_L increases with f (blocks high frequency); X_C decreases with f (passes high frequency).

4. **Forgetting units** — P is in Watts, Q in VAR, S in VA. Mixing these up loses marks.

5. **Power factor direction** — RL circuit → lagging PF; RC circuit → leading PF.

---

## 18. Exam Priority Summary

| Topic | Expected Marks | Depth Needed |
|-------|---------------|--------------|
| RL Circuit (Z, phasor, φ, numerical) | 5 marks | Full formula + diagram |
| RC Circuit (Z, phasor, φ, numerical) | 5 marks | Full formula + diagram |
| Power Triangle (P, Q, S, cos φ) | 10 marks (sub-question) | Diagram + all formulas |
| RMS and Average value | 2–5 marks | Formula + brief derivation |
| RLC / Resonance | 1–2 marks recall | Formula only |
| Phasor concept | 1 mark | Definition |
