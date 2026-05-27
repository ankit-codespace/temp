# Module 5 — Transducers
### Basic Electrical & Electronics Engineering (UEC101T)

---

## 1. What is a Transducer?

A transducer is a device that **converts one form of energy into another**. In electrical engineering, we specifically care about transducers that convert a **physical quantity** (like displacement, temperature, pressure) into an **electrical signal** (voltage or current) — because electrical signals are easy to measure, transmit, and process.

**Example:** A microphone converts sound energy → electrical signal. A thermocouple converts heat → voltage.

> **Exam-ready definition:** A transducer is a device that converts a non-electrical physical quantity into a proportional electrical signal.

---

## 2. Block Diagram of a Transducer System

```
[Physical Quantity]  →  [Sensing Element]  →  [Signal Conditioning]  →  [Electrical Output]
  (Measurand)             (Primary transducer)    (Secondary transducer)    (Voltage / Current)
```

**What each block does:**

- **Sensing Element (Primary Transducer):** Directly responds to the physical quantity. It converts the measurand into a mechanical or intermediate signal. *(Example: a bourdon tube converts pressure into mechanical displacement.)*
- **Signal Conditioning (Secondary Transducer):** Converts that intermediate signal into an electrical output. *(Example: a strain gauge converts displacement into resistance change, which is then read as voltage.)*
- **Electrical Output:** The final signal that goes to a display, recorder, or controller.

> Some transducers do both steps in one element — like LVDT. They sense and convert directly to electrical output.

---

## 3. Classification of Transducers

### 3.1 Based on the Stage of Conversion

| Type | What it does | Example |
|------|-------------|---------|
| **Primary Transducer** | Converts the measurand into a mechanical/intermediate form | Bourdon tube (pressure → displacement) |
| **Secondary Transducer** | Converts that intermediate form into an electrical signal | LVDT (displacement → voltage) |

> Most practical measurement systems use **both** in series. The bourdon tube + LVDT combination measures pressure as a final electrical output.

---

### 3.2 Based on Power Requirements

| Type | How it works | Example |
|------|-------------|---------|
| **Active Transducer** | **Generates its own electrical output** — no external power supply needed | Thermocouple, piezoelectric crystal, photovoltaic cell |
| **Passive Transducer** | **Changes its electrical property** (resistance, capacitance, inductance) — needs external excitation to produce output | LVDT, strain gauge, thermistor, capacitive sensor |

**Simple way to remember:**
- Active → **self-powered** → think of it like a battery — it generates EMF on its own
- Passive → **externally powered** → it changes a property, you need to supply power to detect that change

---

### 3.3 Other Classification Types (for 1-mark / Section A)

| Basis | Types |
|-------|-------|
| Output type | Analog (LVDT, thermocouple) vs Digital (encoder) |
| Measurand type | Displacement, temperature, pressure, force, flow |
| Transduction principle | Resistive, inductive, capacitive, piezoelectric, photoelectric |

---

## 4. Characteristics of a Good Transducer

A good transducer should have:

- **High sensitivity** — small change in input → measurable output change
- **Linearity** — output should be proportional to input across the operating range
- **High accuracy and repeatability** — same input always gives same output
- **Fast response** — output should track input without lag
- **No loading effect** — the transducer should not disturb the quantity it's measuring
- **Ruggedness** — ability to withstand overloads and harsh environments

---

## 5. LVDT — Linear Variable Differential Transformer

**This is the most important topic of Module 5. Expect it at 5-mark or 10-mark depth in exams.**

---

### 5.1 What is LVDT?

LVDT stands for **Linear Variable Differential Transformer**. It is a **passive, inductive transducer** that measures **linear displacement** and converts it into a proportional AC voltage output.

It is one of the most widely used transducers because:
- Output is **linear** over a wide range
- It is **contactless** (the core doesn't touch the coil — no wear)
- Very accurate and repeatable

---

### 5.2 Construction

The LVDT consists of:

1. **One Primary Coil (P)** — placed at the center, connected to an AC supply (excitation)
2. **Two Secondary Coils (S₁ and S₂)** — placed symmetrically on either side of the primary, wound in **opposite directions** (connected in series opposition)
3. **Ferromagnetic Core** — a soft iron or ferrite rod that slides freely inside the coil assembly without touching it
4. **Cylindrical Former** — non-magnetic housing that holds all the coils

```
          ┌──────────────────────────────────┐
          │   S₁       Primary (P)      S₂   │
          │  ┌───┐      ┌──────┐       ┌───┐ │
 AC ──────┤  │███│      │██████│       │███│ ├──── Output (S₁ - S₂)
 Supply   │  └───┘      └──────┘       └───┘ │
          │         [← Core slides →]         │
          └──────────────────────────────────┘
```

**Labels for diagram:**
- P = Primary coil (center)
- S₁ = First secondary coil (left)
- S₂ = Second secondary coil (right)
- Core = Ferromagnetic sliding rod
- Output = Differential voltage (E₁ − E₂)

> The two secondary coils are wound in **opposite directions** and connected in **series opposition** — this is the key design choice that makes the output zero at center and proportional to displacement.

---

### 5.3 Working Principle

The primary coil is energized with an AC supply. This creates a changing magnetic flux, which **induces voltages** in both secondary coils (E₁ in S₁ and E₂ in S₂).

The **output voltage = E₁ − E₂** (differential output).

What happens depends on **where the core is:**

---

**Case 1 — Core at Null Position (Center)**

The core is exactly between S₁ and S₂. Flux linking both secondaries is **equal**.

→ E₁ = E₂  
→ Output = E₁ − E₂ = **0 V**

This is called the **null position**. It serves as the reference point (zero displacement).

---

**Case 2 — Core moved toward S₁ (Positive Displacement)**

More flux links S₁, less flux links S₂.

→ E₁ > E₂  
→ Output = E₁ − E₂ = **positive voltage**  
→ Output is **in phase** with the primary supply voltage

---

**Case 3 — Core moved toward S₂ (Negative Displacement)**

More flux links S₂, less flux links S₁.

→ E₂ > E₁  
→ Output = E₁ − E₂ = **negative voltage**  
→ Output is **180° out of phase** with the primary supply voltage

---

### 5.4 Output Characteristic Curve

```
Output
Voltage
  |                  /
  |                 /
  |                /
--+---------------+------------- Displacement
  |        NULL  /
  |             /
  |            /
  |           /
  (−)        (+)
```

More accurately:

```
Output
Voltage
(+)     |         /
        |        /
        |       /  ← Linear region
        |      /
        |     0 ← NULL point
        |      \
        |       \
        |        \
(−)     |         \
        |__________\____________ Displacement
        −x     0     +x
```

**Key points from the curve:**
- The curve is **linear** in the operating range (this is what makes LVDT accurate)
- At **null position**, output = 0
- For **positive displacement**, output is a positive voltage **in phase** with supply
- For **negative displacement**, output is same magnitude but **180° phase shifted** (appears as negative)
- The slope of the line = **sensitivity** of the LVDT (V/mm)

> **How LVDT gives direction:** The phase of the output (0° or 180°) tells you which side the core moved. The magnitude tells you how far.

---

### 5.5 How Displacement is Measured

The object whose displacement needs to be measured is **mechanically attached to the LVDT core**.

When the object moves, the core moves with it. The output voltage magnitude tells you **how much** it moved, and the phase tells you **which direction**.

A **phase-sensitive detector** circuit is used at the output to distinguish between positive and negative displacements and give a DC output proportional to displacement.

---

### 5.6 Advantages of LVDT

- **No friction** — core doesn't touch the coil body, so there is no mechanical wear
- **Infinite resolution** — even extremely small displacements can be detected
- **Linear output** over a good operating range
- **High sensitivity** — typically 10–300 mV/mm
- **Robust and reliable** — works in harsh industrial environments
- **No hysteresis** — no magnetic memory issues

---

### 5.7 Disadvantages of LVDT

- Requires **AC excitation** supply
- Output needs additional **signal conditioning** (demodulation) to get a DC output
- Sensitive to **temperature changes** and **stray magnetic fields**
- The core must be kept perfectly aligned — **misalignment causes error**

---

### 5.8 Applications of LVDT

- Measuring **linear displacement** in machine tools
- **Pressure measurement** (when used with a diaphragm as the primary transducer)
- **Force/load measurement** (used with a proving ring)
- Aircraft control surface position sensing
- Civil engineering: measuring structural deformation

---

## 6. Comparison — Active vs Passive Transducer

| Feature | Active Transducer | Passive Transducer |
|---------|------------------|-------------------|
| Power supply needed | No | Yes |
| Generates EMF | Yes (self-generating) | No |
| Output | Direct voltage/current | Change in R, L, or C |
| Example | Thermocouple, piezoelectric | LVDT, thermistor, strain gauge |
| Accuracy | Moderate | Generally higher |

---

## 7. Digital Multimeter (DMM) — Brief Overview *(Tier 3 — Low Exam Priority)*

A **Digital Multimeter** is an instrument that measures voltage, current, and resistance, and displays the result digitally.

**It works using:**
1. An **analog-to-digital converter (ADC)** that converts the measured analog signal into a digital number
2. A **digital display** (usually LCD) that shows the reading

**Key blocks inside a DMM:**
```
Input → Attenuator/Amplifier → ADC → Digital Display
```

- For voltage: the input signal is attenuated to a safe level and fed to the ADC
- For current: the input passes through a **shunt resistor**, voltage across it is measured
- For resistance: the DMM applies a known current and measures the resulting voltage (uses Ohm's law internally)

**Why it's better than analog meters:**
- No parallax error (reading is direct and unambiguous)
- High input impedance → minimal loading effect on the circuit
- Auto-ranging in modern DMMs

---

## 8. Quick Revision Summary

| Topic | Key Point |
|-------|-----------|
| Transducer | Converts physical quantity → electrical signal |
| Primary transducer | Converts measurand → intermediate form |
| Secondary transducer | Converts intermediate → electrical |
| Active transducer | Self-generating (thermocouple, piezo) |
| Passive transducer | Needs excitation (LVDT, strain gauge) |
| LVDT full form | Linear Variable Differential Transformer |
| LVDT — null position | Core at center → E₁ = E₂ → Output = 0 |
| LVDT — positive displacement | Core toward S₁ → E₁ > E₂ → in-phase output |
| LVDT — negative displacement | Core toward S₂ → E₂ > E₁ → 180° phase shift |
| LVDT direction detection | Phase of output (0° or 180°) |
| LVDT magnitude detection | Amplitude of output voltage |
| LVDT major advantage | Contactless → no friction, no wear |

---

## 9. Likely Exam Questions — Module 5

**1-mark (Section A):**
- What is a transducer?
- Differentiate active and passive transducer with one example each
- What is the output of LVDT at null position?
- Name two examples of active transducers
- What does LVDT measure?

**5-mark (Section B):**
- Explain primary and secondary transducers with examples and block diagram
- Classify transducers based on energy conversion and power requirements
- Describe the construction and working of LVDT with a neat diagram

**10-mark (Section C):**
- Explain the construction, working, and output characteristic of LVDT. How is direction and magnitude of displacement determined?
- Describe the classification of transducers. Explain LVDT in detail with diagram and characteristic curve.

---

> **Diagram tip for LVDT:** Always label — Primary coil (P), Secondary coils (S₁ and S₂), Ferromagnetic core, AC supply input, Output (E₁ − E₂). In the characteristic curve, mark null point, linear region, and show phase reversal across the null point.
