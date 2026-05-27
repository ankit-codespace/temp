# BEEE — Module 1: DC Circuits & Network Theorems
**Subject:** Basic Electrical and Electronics Engineering (UEC101T)
**Exam Weight:** High — KCL/KVL and all three theorems are 5–10 mark questions

---

## 1. Basic Concepts (Quick Recall)

**Electric Current (I):** The flow of electrons through a conductor. Measured in Amperes (A).

**Voltage (V):** The electrical pressure that drives current through a circuit. Measured in Volts (V).

**Resistance (R):** Opposition offered to current flow. Measured in Ohms (Ω).

### Ohm's Law

$$V = IR$$

Voltage = Current × Resistance. This is the foundation of every DC circuit calculation.

### Series and Parallel Circuits

| Property | Series | Parallel |
|----------|--------|----------|
| Current | Same through all | Divides across branches |
| Voltage | Divides across elements | Same across all |
| Total Resistance | R = R₁ + R₂ + R₃ | 1/R = 1/R₁ + 1/R₂ + 1/R₃ |

---

## 2. Kirchhoff's Laws

> **Exam weight: 10 marks** — Both laws together are a classic Section C question. Know statements + sign convention + how to apply them together.

### KCL — Kirchhoff's Current Law

**Statement:** The total current entering a node equals the total current leaving it.

In other words, charge cannot accumulate at a junction. Whatever comes in must go out.

$$\sum I_{in} = \sum I_{out}$$

**How to apply:**
1. Identify all nodes (junction points) in the circuit.
2. At each node, write the KCL equation: currents entering = currents leaving.
3. Solve the resulting simultaneous equations.

**Sign Convention:** Currents entering a node are positive (+). Currents leaving are negative (−). Or fix one convention and stick to it throughout.

**Example:** At a node, if I₁ and I₂ enter and I₃ leaves:
$$I_1 + I_2 = I_3$$

---

### KVL — Kirchhoff's Voltage Law

**Statement:** The algebraic sum of all voltages around any closed loop in a circuit is zero.

The idea is simple: if you start at any point in a circuit and travel around a complete loop back to the same point, the total voltage rise equals the total voltage drop.

$$\sum V = 0 \quad \text{(around any closed loop)}$$

**How to apply (Mesh Analysis):**
1. Assign mesh currents (I₁, I₂, ...) to each independent loop — usually clockwise.
2. For each mesh, write KVL: sum of voltage drops = sum of EMF sources.
3. Voltage drop across a resistor = I × R (use the mesh current, or the difference if two meshes share a branch).
4. Solve the equations simultaneously.

**Sign Convention:**
- When tracing a loop and you move through a resistor **in the direction of assumed current** → voltage drop = −IR
- When you move **against current direction** → voltage rise = +IR
- For a source: moving from − to + is a voltage rise; + to − is a drop.

**Two-mesh example setup:**

For Loop 1: $V_1 - I_1 R_1 - (I_1 - I_2) R_3 = 0$

For Loop 2: $-I_2 R_2 - (I_2 - I_1) R_3 - V_2 = 0$

Solve for I₁ and I₂ → use them to find branch currents and voltages.

> **Common mistake:** Forgetting to account for the shared branch current $(I_1 - I_2)$ when two mesh currents pass through the same resistor. The net current in a shared branch is always the algebraic difference of the two mesh currents.

---

## 3. Superposition Theorem

> **Exam weight: 10 marks** — Expect a numerical. The method is systematic — learn the steps, not just the concept.

### What it says

In a circuit with **multiple independent sources**, the current (or voltage) at any element equals the **algebraic sum** of the contributions from each source acting alone.

### How to Apply (Step-by-Step)

1. **Take one source at a time.** Leave one source active; deactivate all others.
2. **Deactivating a source:**
   - Voltage source → replace with a **short circuit** (wire)
   - Current source → replace with an **open circuit** (remove it)
3. **Find the current/voltage** in the required element due to the active source.
4. **Repeat** for each remaining source.
5. **Algebraically add** all partial results. (Respect direction/sign — currents in the same direction add, opposite directions subtract.)

### Important Points

- Works only for **linear circuits** (circuits with resistors, linear inductors, capacitors — not diodes or transistors).
- Does NOT apply directly to **power** (power is not a linear quantity). Calculate current first, then find power.
- Each partial circuit is solved using basic Ohm's law and series/parallel rules.

> **Common mistake:** Adding powers from each superposition step instead of adding currents/voltages. Always superpose the linear quantities, then calculate power at the end.

---

## 4. Thevenin's Theorem

> **Exam weight: 5–10 marks** — Statement + circuit diagram + numerical. All three may appear together. A very reliable question.

### What it says

Any linear circuit with sources and resistors, viewed from two terminals (A and B), can be replaced by:
- A **single voltage source** V_th (open-circuit voltage at A–B)
- In **series** with a **single resistance** R_th (the equivalent resistance seen from A–B with all sources deactivated)

This simplified circuit is called the **Thevenin Equivalent Circuit.**

### Why it's useful

When you need to find the current through a load for multiple load values, redoing the full circuit each time is inefficient. Thevenin reduces the whole network to one source + one resistor. Then finding IL for any RL is just one equation.

### Steps to Find Thevenin Equivalent

1. **Remove the load** R_L (open-circuit the terminals A and B).
2. **Find V_th** = voltage across the open terminals A–B (use KVL or voltage divider).
3. **Deactivate all sources:**
   - Voltage source → short circuit
   - Current source → open circuit
4. **Find R_th** = equivalent resistance seen from terminals A–B (with load removed and sources deactivated).
5. **Draw the Thevenin equivalent:** V_th in series with R_th, then reconnect R_L.
6. **Find load current:** 
$$I_L = \frac{V_{th}}{R_{th} + R_L}$$

### Thevenin Equivalent Circuit (Diagram Description)

```
    A ──┬─── R_th ───┬──> (to load R_L)
        |            |
       V_th          |
        |            |
    B ──┴────────────┘
```
**Must-label in diagram:** V_th, R_th, terminals A and B, load R_L.

> **Common mistake:** Finding R_th without deactivating sources first. Voltage sources must be shorted and current sources must be opened before calculating R_th.

---

## 5. Norton's Theorem

> **Exam weight: 10 marks** — Often paired with Thevenin in a Section C question. Verify your answer using the relationship between both equivalents.

### What it says

Any linear circuit, viewed from two terminals, can be replaced by:
- A **single current source** I_N (short-circuit current at A–B)
- In **parallel** with a **single resistance** R_N

R_N is found the exact same way as R_th. In fact, **R_N = R_th always**.

### Steps to Find Norton Equivalent

1. **Remove the load** R_L.
2. **Short-circuit terminals A and B** (put a wire across them).
3. **Find I_N** = current flowing through this short circuit (use KVL or current divider).
4. **Find R_N** = same method as R_th (deactivate sources, find equivalent resistance from terminals).
5. **Draw the Norton equivalent:** I_N in parallel with R_N, then reconnect R_L.
6. **Find load current using current divider:**
$$I_L = I_N \times \frac{R_N}{R_N + R_L}$$

### Norton Equivalent Circuit (Diagram Description)

```
    A ──┬─────────────┬──> (to load R_L)
        |             |
       I_N  ↑        R_N
        |             |
    B ──┴─────────────┘
```
**Must-label in diagram:** I_N (with arrow showing direction), R_N, terminals A and B, load R_L.

### Relationship Between Thevenin and Norton

$$V_{th} = I_N \times R_N \qquad R_{th} = R_N$$

This is **source transformation**. If you have one equivalent, you can directly get the other. Use this to cross-check your answer in numericals.

> **Common mistake:** Forgetting to short the terminals when finding I_N. Many students find the open-circuit voltage instead of the short-circuit current — that gives V_th, not I_N.

---

## 6. Comparison: The Three Theorems

| Feature | Superposition | Thevenin | Norton |
|---------|--------------|----------|--------|
| Purpose | Find response due to multiple sources | Simplify circuit to one voltage source + R | Simplify circuit to one current source + R |
| Equivalent | No single equivalent — sum of parts | V_th in series with R_th | I_N in parallel with R_N |
| When to use | Multiple independent sources | Finding current for various load values | Same as Thevenin; dual form |
| Key calculation | Partial currents for each active source | V_th (open circuit), R_th (deactivated) | I_N (short circuit), R_N (deactivated) |
| Relationship | Independent | R_th = V_th / I_N | R_N = R_th |

---

## 7. Formula Sheet — Module 1

```
Ohm's Law:              V = IR

Series Resistance:      R_total = R1 + R2 + R3

Parallel Resistance:    1/R_total = 1/R1 + 1/R2 + 1/R3

KCL:                    ΣI_in = ΣI_out  (at a node)

KVL:                    ΣV = 0  (around a closed loop)

Thevenin current:       IL = Vth / (Rth + RL)

Norton current (load):  IL = IN × RN / (RN + RL)

Thevenin ↔ Norton:      Vth = IN × RN,   Rth = RN
```

---

## 8. Exam Tips for Module 1

**For KCL/KVL (10-mark question):**
Write both statements clearly first. Then show the circuit, define mesh currents, write KVL equations, and solve step-by-step. Show all working — marks are awarded for process, not just the final answer.

**For Thevenin/Norton numericals:**
Always write these five labels at the start: V_th, R_th, I_N, R_N, I_L. Work through each one methodically. If asked for both equivalents, use the conversion formula to save time — you don't need to solve the full circuit twice.

**For Superposition:**
Draw a separate circuit diagram for each active source. This avoids confusion and also earns diagram marks.

**Section A quick recalls:**
- Thevenin theorem was given by — *Charles de la Sablonière Thévenin (1883)*
- Norton theorem was given by — *Edward Norton (1926)*
- KCL is based on conservation of charge; KVL is based on conservation of energy.
- Superposition applies only to **linear** circuits.
- R_th and R_N are always equal.
