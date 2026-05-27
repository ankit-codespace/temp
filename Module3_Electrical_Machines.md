# Module 3 — Electrical Machines
**Subject:** Basic Electrical & Electronics Engineering (UEC101T)

> **Exam Priority:** Medium-High | Appears in both MSTs at 5-mark level
> **Topics:** Transformer · 3-Phase Induction Motor · DC Motor

---

## 1. Transformer

### What is it?

A transformer transfers electrical energy from one circuit to another using electromagnetic induction — **without any electrical contact** between the two circuits. It can increase (step-up) or decrease (step-down) the AC voltage.

> It works on **Faraday's Law**: a changing magnetic flux induces an EMF in a nearby coil.

---

### Construction

A transformer has three main parts:

1. **Primary coil (winding)** — the input coil. Connected to the AC supply.
2. **Secondary coil (winding)** — the output coil. Connected to the load.
3. **Iron core** — made of laminated silicon steel. Carries the magnetic flux from primary to secondary.

> **Why laminated core?** Thin laminations reduce eddy current losses (heat wastage inside the iron).

**Diagram labels to include:** Primary winding (N₁ turns), Secondary winding (N₂ turns), Laminated iron core, Input (AC supply), Output (Load), Flux path (arrows through core).

---

### Working

When AC flows through the primary coil, it creates a **continuously changing magnetic flux** in the iron core. This changing flux links with the secondary coil and induces an EMF in it (mutual induction).

The secondary voltage depends on the turns ratio:

$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}$$

| Variable | Meaning |
|---|---|
| V₁, V₂ | Primary and secondary voltage |
| N₁, N₂ | Number of turns in primary and secondary |
| I₁, I₂ | Primary and secondary current |

> Note: When voltage steps up, current steps down proportionally. Power is conserved (ideally).

---

### Step-Up vs Step-Down

| Type | Condition | Example Use |
|---|---|---|
| Step-up | N₂ > N₁ → V₂ > V₁ | Power transmission (high voltage, low current = less loss) |
| Step-down | N₂ < N₁ → V₂ < V₁ | Home appliances, mobile chargers |

---

### Why Transformer Fails on DC ⚠️

This is a classic exam question.

DC produces a **constant (steady) current**. A constant current creates a **constant magnetic flux** — it does not change with time.

Since there is **no change in flux**, there is **no induced EMF** in the secondary coil. So the transformer simply does not work on DC.

> **One-line exam answer:** A transformer works only on AC because it requires a changing magnetic flux to induce EMF. DC produces constant flux, so no EMF is induced in the secondary.

**Bonus:** On DC, the primary behaves like a pure resistor. If the DC supply is high enough, the primary winding can overheat and burn out.

---

### Important Formulas

| Formula | Use |
|---|---|
| N₁/N₂ = V₁/V₂ | Find secondary voltage or turns |
| N₁/N₂ = I₂/I₁ | Find secondary current |
| Efficiency η = (Output Power / Input Power) × 100% | Ideal transformer: η = 100% |

---

## 2. Three-Phase Induction Motor (3-phase IM)

### What is it?

A 3-phase induction motor is the most widely used AC motor in industry. It converts three-phase electrical energy into mechanical rotation. The rotor is not electrically connected to the supply — it gets its energy purely through induction (like a transformer's secondary coil).

---

### Working Principle

1. Three-phase AC supply is given to the **stator** (stationary outer part) windings.
2. This creates a **Rotating Magnetic Field (RMF)** inside the motor — the field physically rotates at synchronous speed.
3. This rotating field cuts across the **rotor** conductors, inducing an EMF (Faraday's Law).
4. The induced EMF drives a current through the rotor conductors.
5. This current-carrying rotor sits inside a magnetic field → force is produced (Lorentz force) → rotor starts to rotate.

> The rotor always rotates **slightly slower** than the rotating field. This speed difference is essential — if they ran at the same speed, there would be no relative motion, no induced EMF, and no torque.

---

### Synchronous Speed

The speed of the rotating magnetic field (not the rotor itself) is called **synchronous speed**.

$$N_s = \frac{120f}{P}$$

| Variable | Meaning |
|---|---|
| Nₛ | Synchronous speed (rpm) |
| f | Supply frequency (Hz), typically 50 Hz in India |
| P | Number of poles |

**Example:** A 4-pole motor on 50 Hz supply → Nₛ = (120 × 50)/4 = **1500 rpm**

> Quick recall for exams — poles 4, 6, 8, 12 at 50 Hz give: 1500, 1000, 750, 500 rpm

---

### Slip

The rotor always runs slower than Nₛ. The difference is called **slip**.

$$s = \frac{N_s - N}{N_s}$$

Or as a percentage: **s% = [(Nₛ − N) / Nₛ] × 100**

- At standstill (motor just switched on): N = 0, so **s = 1 (100%)**
- At synchronous speed (impossible in practice): N = Nₛ, so **s = 0**
- Normal running: slip is typically **3% to 8%**

---

### Torque-Slip Characteristic Curve ⭐ (5-mark / 10-mark topic)

This curve shows how the torque produced by the motor changes as slip changes (i.e., as rotor speed changes from standstill to synchronous speed).

**Shape of the curve:**

```
Torque ↑
        |         *  ← Maximum (Breakdown) Torque
        |       *   *
        |     *       *
        |   *           *   ← Starting torque (at s=1)
        |  *               *
        | *                  *
        +--------------------------------→ Slip
        0 (Nₛ)              s=1 (standstill)
```

**Diagram labels to include:** Torque (Y-axis), Slip (X-axis, 0 to 1), Starting torque point (s=1), Breakdown/maximum torque point, Full-load torque point (operating region), Stable zone, Unstable zone.

**Key points on the curve:**

| Point | Slip | What's happening |
|---|---|---|
| s = 1 (standstill) | 100% | Motor just started. Starting torque is moderate. |
| s at max torque | ~20–25% | Torque reaches its peak — called **breakdown torque** |
| s = 0 to 25% | Low slip | **Stable operating region** — motor runs here normally |
| s = 25% to 100% | High slip | **Unstable region** — motor won't sustain operation here |

**Why the curve has a peak:**
At low slip (high speed), rotor resistance dominates → torque increases with slip.
At high slip (low speed), rotor reactance dominates → torque decreases with slip.
The peak is where they balance out.

**Significance:**

- **Starting torque** must be enough to overcome static load — if not, the motor won't start.
- **Breakdown torque** is the maximum torque the motor can deliver — if load exceeds this, the motor stalls.
- **Full-load torque** is the normal operating torque — the motor runs in the stable region just to the left of the peak.

---

## 3. DC Motor

### What is it?

A DC motor converts direct current (DC) electrical energy into mechanical rotation. It works on the principle that **a current-carrying conductor placed in a magnetic field experiences a force** (Lorentz force / Fleming's Left-Hand Rule).

---

### Construction

**Diagram labels to include:** Yoke, Field poles, Field winding, Armature core, Armature winding, Commutator, Brushes, Air gap, Shaft.

| Component | What it does |
|---|---|
| **Yoke** | The outer cylindrical frame. Made of cast iron or steel. Provides mechanical support and carries return magnetic flux. |
| **Field poles** | Projecting iron pieces inside the yoke. Create the main magnetic field. |
| **Field winding** | Copper coils wound around the field poles. Current through these coils creates the magnetic field. |
| **Armature core** | Cylindrical laminated iron core. Carries the armature winding and rotates. |
| **Armature winding** | Coils placed in slots on the armature core. Current-carrying conductors that experience force and produce rotation. |
| **Commutator** | Made of copper segments, fixed on the shaft. Converts alternating current inside the armature to unidirectional (DC) current in the external circuit — acts as a mechanical rectifier. |
| **Brushes** | Carbon blocks pressing on the commutator. Maintain electrical contact between the rotating commutator and the external circuit. |
| **Air gap** | Small gap between stator (field poles) and rotor (armature). Magnetic flux crosses this gap. |

---

### Working Principle

1. DC supply is given to the **armature winding** through the brushes and commutator.
2. The **field windings** create a strong magnetic field in the air gap.
3. The armature conductors carry current inside this magnetic field.
4. By **Fleming's Left-Hand Rule**, each conductor experiences a force.
5. Forces on all conductors add up to produce a net **torque**, causing the armature (rotor) to rotate.

> **Fleming's Left-Hand Rule:** Point the index finger in the field direction (N→S), middle finger in current direction — the thumb points in the direction of force on the conductor.

---

### Types of DC Motors (brief)

| Type | Connection | Behaviour |
|---|---|---|
| Series motor | Field in series with armature | Very high starting torque. Speed varies a lot with load. Used in traction (trains, cranes). |
| Shunt motor | Field in parallel with armature | Nearly constant speed. Used in lathes, fans, pumps. |
| Compound motor | Both series + shunt field | Combines properties of both. |

> For exams — if asked about construction, both series and shunt motors have the same physical parts. Only the winding connection differs.

---

## Quick Revision Summary

| Topic | Key Formula / Key Point |
|---|---|
| Transformer turns ratio | N₁/N₂ = V₁/V₂ = I₂/I₁ |
| Why no DC transformer | Constant flux → no EMF induced |
| Synchronous speed | Nₛ = 120f / P |
| Slip | s = (Nₛ − N) / Nₛ |
| Rotor speed at start | 0 rpm → s = 1 |
| Normal slip range | 3% – 8% |
| Stable operating zone | Low slip region (left of peak on torque-slip curve) |
| DC motor principle | Lorentz force on current-carrying conductor in magnetic field |
| Commutator function | Converts internal AC to external DC |
| Series motor use | High starting torque — trains, cranes |
| Shunt motor use | Constant speed — lathes, fans |

---

## Exam Tips

- **Transformer on DC** — this appears as a 1-mark or 2-mark question frequently. Answer in 3 lines: working needs changing flux → AC gives that → DC doesn't.
- **Synchronous speed calculation** — always check pole count carefully (P = number of poles, not pairs). Plug in f = 50 Hz directly.
- **Torque-slip curve** — draw it slowly and neatly. Mark all five key points: s=0, s=1, starting torque, breakdown torque, and the stable/unstable zone boundary. That alone earns most marks.
- **DC motor diagram** — do not forget the commutator and brushes. Many students draw the coil and magnet but miss these — that's where marks are lost.
- **Slip = 0 is impossible** at normal load — if asked, say "synchronous speed is the theoretical maximum; in practice, rotor always lags due to slip."
