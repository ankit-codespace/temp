# Basic Electrical and Electronics Engineering — Revision Notes
### Complete Solved Paper | UEC101T | 30 Marks
### Chandigarh Engineering College | B.Tech AIDS | Sem 2

---

## SECTION A — 1 Mark Each

---

### Q1a) Recall the equivalent circuit of Thevenin's Theorem. [1 Mark]

**Thevenin's theorem** states that any linear circuit can be replaced by a single voltage source **Vth** (open-circuit voltage at the terminals) connected in series with a resistance **Rth** (the equivalent resistance seen from the terminals with all sources deactivated).

[DIAGRAM: A single loop with Vth as voltage source in series with Rth, connected to terminals A and B]

---

### Q1b) Define impedance in AC circuits. Give its units. [1 Mark]

**Impedance (Z)** is the total opposition offered by a circuit to the flow of alternating current. It includes both resistance (R) and reactance (inductive XL or capacitive XC). It is measured in **Ohms (Ω)**.

> Z = √(R² + X²)

---

### Q1c) Irms = 6A, R = 40Ω — find average voltage and peak voltage. [1 Mark]

- Vrms = Irms × R = 6 × 40 = **240 V**
- Vpeak = Vrms × √2 = 240 × 1.414 = **339.4 V**
- Vavg = 0.637 × Vpeak = 0.637 × 339.4 = **216.1 V**

---

### Q1d) Write equation for sinusoidal current: f = 25 Hz, Irms = 20A. [1 Mark]

- Im = Irms × √2 = 20 × 1.414 = **28.28 A**
- ω = 2πf = 2π × 25 = 50π rad/s

> **i = 28.28 sin(50πt) A**

---

### Q1e) Name materials used for transformer core and windings. [1 Mark]

**Core:** Silicon steel (soft iron laminated sheets) — used because it has high permeability and low hysteresis loss.

**Windings:** Copper — used because of its low resistivity and good conductivity.

---

## SECTION B — 5 Marks Each

---

### Q2 — Option 1: Summarize the analysis of RL circuit. [5 Marks]

In a series **RL circuit**, a resistor R and an inductor L are connected in series to an AC supply of voltage V.

[DIAGRAM: Series RL circuit with AC source V, resistor R, and inductor L in a single loop, with phasor diagram showing VR along horizontal, VL vertical, V as resultant]

**1. Voltage relationships:**
The voltage across R is VR = IR, which is in phase with the current. The voltage across L is VL = IXL, which leads the current by 90°. Since these are 90° apart, total voltage is found by phasor addition:

> V = √(VR² + VL²)

**2. Impedance:**
Z = √(R² + XL²), where XL = 2πfL is the inductive reactance in Ohms.

**3. Phase angle:**
The current lags the supply voltage by angle φ, where:

> tan φ = XL/R → φ = tan⁻¹(XL/R)

**4. Power factor:**
cos φ = R/Z (lagging, since current lags voltage in an inductive circuit)

**5. Current:**
I = V/Z

Key point: the higher the frequency, the greater XL becomes, so the circuit becomes more inductive and the phase lag increases.

---

### Q2 — Option 2: Define AC Terms in Detail. [5 Marks]

**i. Instantaneous Value:**
The value of an alternating quantity (voltage or current) at any specific instant of time. It keeps changing every moment as the waveform cycles. Represented as v = Vm sin(ωt) where the value depends on the time t you pick.

**ii. Peak-to-Peak Value:**
The total voltage swing from the maximum positive value to the maximum negative value in one complete cycle. If peak value is Vm, then:

> Peak-to-peak value = 2Vm

For example, if Vm = 20V, the peak-to-peak value is 40V.

**iii. Average Value:**
The mean of all instantaneous values over one half-cycle of the AC waveform (taken over half cycle because the full cycle averages to zero for a sinusoidal wave).

> Vavg = 0.637 × Vm = (2/π) × Vm

**iv. Equation for sinusoidal voltage — f = 50 Hz, Vm = 20V:**

> v = Vm sin(2πft) = 20 sin(2π × 50 × t)
>
> **v = 20 sin(100πt) Volts**

[DIAGRAM: Sinusoidal voltage vs time graph, showing one full cycle from 0 to 0.02s, peak at +20V at t=5ms, zero crossing at t=10ms, trough at -20V at t=15ms, x-axis labeled time in ms, y-axis labeled voltage in V]

---

### Q3 — Option 1: Derive RMS value of alternating current in terms of maximum value. [5 Marks]

**RMS (Root Mean Square)** value is the DC equivalent value of an AC current — the steady DC that would produce the same heating effect in a resistor.

**1. Expression for instantaneous current:**
> i = Im sin(ωt)

**2. Square of instantaneous current:**
> i² = Im² sin²(ωt)

**3. Mean value of i² over one full cycle:**
Using the identity: sin²(ωt) averaged over a full cycle = 1/2

> Mean of i² = Im²/2

**4. Take square root to get RMS:**
> Irms = √(Im²/2) = Im/√2
>
> **Irms = 0.707 × Im**

This is the most important result in AC theory. It means the RMS value is always 70.7% of the peak value.

**Significance:** When we say household supply is 230V, that is the RMS value. The actual peak voltage is 230 × √2 ≈ 325V. All AC meters read RMS values.

---

### Q3 — Option 2: Impedance and power factor of an RC circuit. [5 Marks]

In a series **RC circuit**, a resistor R and capacitor C are connected in series to an AC supply.

[DIAGRAM: Series RC circuit with AC source V, resistor R, and capacitor C, with phasor diagram showing VR horizontal (in phase with I), VC downward (lags current by 90°), and V as resultant below horizontal]

**1. Voltage across R:** VR = IR (in phase with current)

**2. Voltage across C:** VC = IXC, where XC = 1/(2πfC) — this lags the current by 90°

**3. Capacitive Reactance:**
> XC = 1/(2πfC)

As frequency increases, XC decreases — a capacitor passes high-frequency AC more easily.

**4. Impedance:**
> Z = √(R² + XC²)

**5. Phase angle:**
The current leads the voltage by angle φ (opposite of RL circuit):

> tan φ = XC/R → φ = tan⁻¹(XC/R)

Current leads voltage in a capacitive circuit.

**6. Power Factor:**
> cos φ = R/Z (leading)

The power factor tells how much of the apparent power is actually doing useful work. A PF of 1 means pure resistive circuit; PF close to 0 means mostly reactive (no real power consumed).

---

### Q4 — Option 1: Interpret step-up and step-down transformers. [5 Marks]

A **transformer** transfers electrical energy from one circuit to another through electromagnetic induction, with a change in voltage level.

[DIAGRAM: Transformer with laminated core, primary coil N1 turns on left, secondary coil N2 turns on right, input V1 on primary side, output V2 on secondary side]

The governing equation is:
> V1/V2 = N1/N2 = I2/I1

where N1, N2 = number of turns; V1, V2 = voltages; I1, I2 = currents.

**Step-Up Transformer:**
N2 > N1, so V2 > V1. It increases the voltage from primary to secondary. Current on the secondary side decreases proportionally (since power is conserved: V1I1 = V2I2). Used in power transmission lines where high voltage is needed to reduce current and minimize losses.

**Step-Down Transformer:**
N1 > N2, so V2 < V1. It decreases the voltage. Current on the secondary side increases. Used in household distribution to step 11kV or 33kV down to 230V for home use.

In both cases, power is ideally conserved (ignoring losses): Input VA = Output VA.

---

### Q4 — Option 2: Why does a transformer fail to operate on DC? [5 Marks]

A transformer is designed exclusively for AC. When DC is applied, it fails to function and may actually be damaged. Here is why:

**1. Transformer operates on Faraday's law:**
The induced EMF in the secondary coil is e = −N dΦ/dt. An EMF is only induced when the magnetic flux is changing (dΦ/dt ≠ 0).

**2. DC produces constant flux:**
Direct current is steady. A steady current in the primary creates a constant magnetic flux in the core. Since flux is not changing, dΦ/dt = 0, so no EMF is induced in the secondary. Energy transfer fails completely.

**3. No back EMF in primary:**
In AC operation, the changing flux induces a back EMF in the primary that limits the current. With DC, there is no changing flux, so no back EMF is generated.

**4. Primary acts as a low-resistance wire:**
The DC resistance of the primary winding is very small (just the winding's copper resistance, typically a few ohms). Without back EMF, an extremely large current flows through the primary.

**5. Result — overheating and failure:**
This massive current causes severe I²R heating, burns the insulation, and destroys the winding within seconds.

In short: a transformer needs a changing flux to function — and only AC can create that. DC gives constant flux, zero output, and a burnt primary coil.

---

## SECTION C — 10 Marks

---

### Q5a) Power triangle — active, reactive, and apparent power. [~5 Marks]

In any AC circuit containing resistance and reactance, three types of power exist simultaneously:

[DIAGRAM: Right-angled triangle with horizontal side labeled P (Active Power, Watts), vertical side labeled Q (Reactive Power, VAR), hypotenuse labeled S (Apparent Power, VA), angle φ at the base between S and P]

**1. Active Power (P):**
Also called real power or true power. This is the power actually consumed and converted to heat, light, or mechanical work.

> P = VI cos φ &nbsp;&nbsp; (unit: Watts, W)

**2. Reactive Power (Q):**
Power that oscillates between source and reactive components (inductors and capacitors) without doing useful work.

> Q = VI sin φ &nbsp;&nbsp; (unit: Volt-Ampere Reactive, VAR)

**3. Apparent Power (S):**
The total power supplied by the source — the product of RMS voltage and current, without considering phase.

> S = VI &nbsp;&nbsp; (unit: Volt-Ampere, VA)

**4. Relationship (Pythagoras applied to power):**
> S² = P² + Q²

**5. Power Factor:**
> cos φ = P/S = Active Power / Apparent Power

A power factor of 1 means all power is active (purely resistive). A low power factor means most power is reactive — inefficient. Power factor correction (using capacitors) is done in industries to bring PF close to 1.

---

### Q5b) Superposition Theorem — find current through 20Ω. [~5 Marks]

**Superposition theorem** states that in a circuit with multiple sources, the current through any branch equals the algebraic sum of currents produced by each source acting independently, while all other sources are deactivated (voltage sources → shorted, current sources → open-circuited).

Circuit: 20V source, 5Ω, 10Ω (vertical middle branch), 10Ω (horizontal), 20Ω, and 4A current source.

[DIAGRAM: Circuit with nodes — 20V source on left, 5Ω connecting to middle junction node, 10Ω vertical from junction to ground, 10Ω horizontal from junction to right node, 20Ω vertical from right node to ground, 4A current source from ground pointing up into right node]

#### Step 1 — Deactivate 4A source (open circuit it), keep 20V source:

Using node analysis (V₂ = middle junction, V₃ = right node):

At V₃: (V₂ − V₃)/10 = V₃/20 → 2V₂ − 2V₃ = V₃ → V₂ = 3V₃/2

At V₂: (20 − V₂)/5 = V₂/10 + (V₂ − V₃)/10

Substituting V₂ = 3V₃/2 and solving:

> 40 = 5V₃ → **V₃ = 8V**
>
> I'₂₀ = V₃/20 = 8/20 = **0.4 A** (downward through 20Ω)

#### Step 2 — Deactivate 20V source (short it), keep 4A source:

With 20V shorted, 5Ω connects from the junction to ground.

Equivalent resistance from junction to ground:
> 5Ω ∥ 10Ω = 10/3 Ω

At right node V₃: 4A enters node. Two parallel paths to ground:
- Path 1: 20Ω directly
- Path 2: 10Ω + 10/3 Ω = 40/3 Ω

> Equivalent: 20 ∥ (40/3) = (20 × 40/3)/(20 + 40/3) = (800/3)/(100/3) = **8Ω**
>
> V₃ = 4A × 8Ω = 32V
>
> I''₂₀ = 32/20 = **1.6 A** (downward through 20Ω)

#### Final Answer:

Both currents flow in the same direction through 20Ω:

> **I₂₀ = I'₂₀ + I''₂₀ = 0.4 + 1.6 = 2 A**

---

### OR

---

### Q5c) Explain KCL and KVL with significance. [~5 Marks]

**Kirchhoff's Current Law (KCL):**
At any node (junction) in a circuit, the sum of all currents entering the node equals the sum of all currents leaving the node.

> ΣI(entering) = ΣI(leaving)

Or equivalently: the algebraic sum of all currents at a node = 0.

[DIAGRAM: Junction node with three branches — I1 and I2 entering from left and top, I3 leaving to the right, labeled with KCL equation I1 + I2 = I3]

This is based on the conservation of charge — charge cannot accumulate at a node.

**Kirchhoff's Voltage Law (KVL):**
Around any closed loop in a circuit, the algebraic sum of all voltages (EMFs and voltage drops) equals zero.

> ΣV = 0

[DIAGRAM: Single closed loop with voltage source V, resistors R1 and R2, showing voltage rises and drops, with KVL equation V − IR1 − IR2 = 0]

This is based on the conservation of energy — energy gained from sources equals energy lost across resistances.

**Significance in circuit analysis:**
KCL and KVL are the foundation of all circuit analysis methods — mesh analysis, node voltage method, Thevenin's, Norton's, and superposition all derive their equations using these two laws. They apply to all linear and nonlinear circuits, DC or AC, and allow engineers to solve circuits of any complexity by writing simple algebraic equations.

---

### Q5d) Norton's Theorem — find current and voltage across RL = 1.5Ω. [~5 Marks]

**Norton's theorem** states that any linear circuit can be replaced by an equivalent circuit consisting of a current source **IN** in parallel with a resistance **RN**, connected to the load terminals.

Circuit: 12V source, 3Ω (left series), 6Ω (middle shunt), 3Ω (right series), RL = 1.5Ω at terminals A–B.

[DIAGRAM: Circuit with 12V source on left, 3Ω in top branch from source to middle node, 6Ω from middle node to ground, 3Ω in top branch from middle node to terminal A, RL = 1.5Ω from terminal A to terminal B (ground)]

#### Step 1 — Find Norton Current IN (short A–B, find Isc):

With A–B shorted, the right 3Ω connects the middle node directly to ground.

KCL at middle node (voltage = V₁):
> (12 − V₁)/3 = V₁/6 + V₁/3

Multiply through by 6:
> 2(12 − V₁) = V₁ + 2V₁
> 24 − 2V₁ = 3V₁
> V₁ = 4.8V

> **IN = Isc = V₁/3 = 4.8/3 = 1.6 A**

#### Step 2 — Find Norton Resistance RN (deactivate 12V source, short it):

Looking into terminals A–B:

Left 3Ω is now in parallel with 6Ω (both go to ground):
> 3 ∥ 6 = (3 × 6)/(3 + 6) = 18/9 = 2Ω

This 2Ω is in series with the right 3Ω:
> **RN = 2 + 3 = 5Ω**

#### Step 3 — Draw Norton equivalent and solve:

[DIAGRAM: Norton equivalent circuit — 1.6A current source in parallel with RN = 5Ω, connected to RL = 1.5Ω across terminals A and B]

Using current divider:
> IL = IN × RN/(RN + RL) = 1.6 × 5/(5 + 1.5) = 8/6.5

> **IL = 1.23 A**

> **VL = IL × RL = 1.23 × 1.5 = 1.85 V**

#### Summary of Results:

| Parameter | Value |
|-----------|-------|
| Norton Current (IN) | 1.6 A |
| Norton Resistance (RN) | 5 Ω |
| Load Current (IL) | 1.23 A |
| Load Voltage (VL) | 1.85 V |

---

*End of Solved Paper — UEC101T Basic Electrical and Electronics Engineering*
