# Module 4 — Electrical Installations
### Subject: Basic Electrical & Electronics Engineering (UEC101T)
> **Priority: HIGHEST** — CO4 contributed 15 marks in MST2 including a full 10-mark Section C question. MCB, ELCB, and Pipe Earthing are all diagram-heavy topics where a neat, labeled drawing alone fetches 3–4 marks.

---

## Topics at a Glance

| Topic | Exam Weight | Type |
|---|---|---|
| MCB | 5–10 marks | Diagram + Explanation |
| ELCB | 10 marks | Diagram + Explanation |
| Pipe Earthing | 10 marks | Diagram + Explanation |
| Wires and Cables | 1–5 marks | Recall + Comparison |
| MCB vs ELCB vs MCCB | 1–2 marks | Short Answer / Table |

---

## 1. Wires and Cables

### What's the difference?

A **wire** is a single conductor. A **cable** is one or more wires bundled together with insulation and a protective outer sheath.

In electrical installations, cables are used because they carry multiple conductors (live, neutral, earth) in one unit and protect them from mechanical damage.

---

### Types of Wires and Cables

#### PVC (Polyvinyl Chloride) Cable
The most common type in household wiring. The insulation is made of PVC plastic, which is cheap, flexible, and resistant to moisture.

- Used in: domestic wiring, light points, switches, fans
- Limitation: cannot handle very high temperatures — the insulation softens above 70°C

#### XLPE (Cross-Linked Polyethylene) Cable
The insulation is chemically treated polyethylene. This treatment (cross-linking) makes it much more heat-tolerant than PVC.

- Can handle temperatures up to 90°C
- Used in: industrial power distribution, underground feeders, high-load circuits
- Better electrical properties and longer lifespan than PVC

#### Armoured Cable (SWA — Steel Wire Armoured)
Has an extra layer of steel wires wound around the cable. This layer protects against physical damage — being stepped on, rodent bites, or being buried underground.

- Used in: underground cables, industrial installations, outdoor wiring
- The steel armour is earthed for safety

#### Flexible Cable (Flex)
Has many fine strands of copper instead of one thick conductor. This makes it bendable without breaking.

- Used in: appliance cords, extension leads, any application where the cable is regularly moved

---

### Conductor Materials

| Material | Property | Where Used |
|---|---|---|
| Copper | High conductivity, flexible, expensive | Most wiring |
| Aluminium | Lighter, cheaper, lower conductivity | Power transmission lines |

---

### Exam Point
PVC coating provides **electrical insulation** and **protection from moisture**. The question "why is PVC used as wire insulation?" appeared directly in MST2 Section A.

---

## 2. MCB — Miniature Circuit Breaker

### What is an MCB?

An MCB is a safety switch that **automatically trips (opens) the circuit** when it detects either an overload current or a short circuit. Once the fault is cleared, it can be manually reset — unlike a fuse, which must be replaced.

Think of it as a reusable fuse that acts faster and more reliably.

---

### Why MCB instead of a fuse?

A fuse melts and needs replacement every time. An MCB trips and resets. MCBs also trip faster and can be set to specific current ratings, making them safer and more practical for modern installations.

---

### Construction

An MCB has two separate tripping mechanisms housed in a compact enclosure:

**1. Bimetallic Strip (Thermal Trip)**
Two metals with different rates of thermal expansion are bonded together. When current exceeds the rated value for a sustained period, heat builds up and the strip bends. This bending action mechanically trips the contacts open.

- Protects against: **overload** (moderate excess current over time)
- Response: slower — takes a few seconds to minutes depending on overload level

**2. Solenoid / Electromagnet (Magnetic Trip)**
A coil wound around an iron core. Under normal current, the magnetic force is weak. During a short circuit, the current spikes instantly — this creates a strong magnetic pull that instantly trips the contacts.

- Protects against: **short circuit** (very high current instantly)
- Response: almost instantaneous (milliseconds)

**3. Arc Chute**
When contacts open under high current, a spark (arc) forms between them. The arc chute is a stack of metal plates that breaks the arc into smaller segments, cooling it rapidly and extinguishing it safely.

**4. Trip Mechanism and Toggle**
The toggle is the external switch. When a fault occurs, the internal latch releases and the toggle jumps to the "tripped" or middle position. After clearing the fault, the user resets it manually.

---

### Diagram — MCB Internal Structure

```
        [ Toggle / Handle ]
               |
        [ Latch Mechanism ]
          /           \
[ Bimetallic Strip ]  [ Solenoid Coil + Iron Core ]
(Thermal Trip)        (Magnetic Trip)
          \           /
        [ Main Contacts ]
               |
          [ Arc Chute ]
               |
          [ Output Terminal ]
```

**Labels your diagram must include:**
- Bimetallic strip
- Solenoid/electromagnet
- Arc chute
- Main contacts (fixed and moving)
- Toggle / operating handle
- Input and output terminals

---

### Working — Three Conditions

**Normal Condition:**
Current is within the rated value. Bimetallic strip stays straight. Solenoid force is weak. Contacts remain closed. Circuit operates normally.

**Overload Condition:**
Current exceeds the rated value but is not extremely high (e.g., too many appliances on one circuit). The bimetallic strip heats up slowly and bends. After some time, it releases the latch and the contacts open. The circuit is disconnected.

**Short Circuit Condition:**
A dead short causes current to spike instantly to many times the rated value. The solenoid generates a strong magnetic field immediately. The plunger is pulled, instantly releasing the latch and opening the contacts. The arc chute suppresses the arc formed.

---

### Exam Points

- MCB has **two protection mechanisms**: thermal (overload) and magnetic (short circuit)
- **Bimetallic strip = overload protection**; **solenoid = short circuit protection**
- MCB is **resettable** — fuse is not
- MCB does **not** protect against earth leakage — that requires an ELCB/RCCB

---

## 3. ELCB — Earth Leakage Circuit Breaker

### What is an ELCB?

An ELCB is a safety device that detects **current leaking to earth** (ground) and immediately disconnects the circuit. It protects humans from electric shock when they accidentally touch a live conductor or a faulty appliance.

MCB protects wiring from damage. ELCB protects people from being the path to earth.

---

### Why ELCB is needed

In a healthy circuit, current goes out through the live wire and returns through the neutral wire. These two currents are equal. If a fault causes some current to flow to earth instead of returning via neutral, the balance is broken. This leaked current can flow through a person's body if they touch the faulty equipment. The ELCB detects this imbalance and trips before the current is enough to kill.

The human body can be killed by as little as 30–50 mA (0.03–0.05 A) flowing through the heart. An ELCB trips at leakage as small as **30 mA** — well below the lethal threshold.

---

### Construction

**Core Balance Current Transformer (CBCT / Sensing Coil)**
The live and neutral wires pass through a toroidal (ring-shaped) core. Under normal conditions, the magnetic fields from the two wires cancel out (they carry equal and opposite currents), so no voltage is induced in the secondary coil wound on the core.

When a leakage occurs, the live current is greater than the neutral current. The fields no longer cancel, and the imbalance induces a small voltage in the secondary coil.

**Trip Coil and Relay**
The voltage from the secondary coil triggers the trip coil. The trip coil energises a relay (or electronic circuit), which releases the latch holding the contacts closed.

**Main Contacts**
These are in series with the main circuit. When the trip coil acts, the contacts open and the circuit is disconnected.

---

### Diagram — ELCB Working

```
          Live Wire  ──────────────────────────────── Load
                        |                      |
                   [ CBCT Core ]         [ Main Contacts ]
                        |
          Neutral Wire ─────────────────────────────── Load

                   Secondary winding on CBCT
                              |
                       [ Trip Coil ]
                              |
                       [ Relay / Latch ]
                              |
                       Opens contacts on fault
```

**Labels your diagram must include:**
- Live wire
- Neutral wire
- Earth wire (fault path)
- Core Balance CT / sensing coil / toroidal core
- Secondary winding
- Trip coil
- Main contacts
- Load

---

### Working — Normal vs Fault

**Normal Condition:**
IL (live current) = IN (neutral current)

Magnetic flux from both wires in the core cancel each other (they flow in opposite directions through the core). Net flux = 0. No EMF induced in secondary. Trip coil unenergised. Contacts remain closed.

**Fault Condition:**
A person touches a faulty live appliance. Current finds a path to earth through the person's body. Now:

IL > IN (some current leaked to earth, not returned via neutral)

Net flux in the core is non-zero. This induces a voltage in the secondary winding. The trip coil is energised. The relay releases the latch. Contacts open instantly — typically within 30 ms.

---

### Exam Points

- ELCB detects **earth leakage**, not overload
- Trips at **30 mA** leakage — this is the standard safety threshold
- Responds in **less than 30 milliseconds** — fast enough to prevent electrocution
- Also called **RCCB** (Residual Current Circuit Breaker) in modern terminology
- ELCB protects **humans**; MCB protects **wiring**
- Both should be used together in a proper installation

---

## 4. Pipe Earthing

### What is Earthing?

Earthing (or grounding) is connecting the metallic body of electrical equipment to the ground (earth) through a low-resistance path. The earth is considered to be at zero potential.

If a live conductor accidentally touches the metal body of an appliance (a fault condition), current flows safely to earth through this connection instead of through a person who touches the appliance.

---

### Why Earthing is Critical

Without earthing, if a live wire touches the metal casing of a washing machine, the casing becomes live at 230 V. Anyone who touches it completes the circuit through their body to ground — they get a severe or fatal shock.

With earthing, the fault current flows harmlessly to earth, and the high current also trips the MCB, disconnecting the supply.

---

### Pipe Earthing — Construction

Pipe earthing uses a **GI (Galvanised Iron) pipe** buried vertically in the ground as the earth electrode.

**Components:**

**GI Pipe:**
- Minimum diameter: 38 mm
- Minimum length buried in ground: 2.5 metres
- Perforated (holes drilled) along its length to allow moisture to reach the surrounding soil and improve conductivity

**Charcoal Layer:**
Packed around the pipe in the pit. Charcoal retains moisture and improves conductivity. Keeps the soil around the pipe moist even in dry seasons.

**Salt Layer:**
Salt (sodium chloride) is added along with charcoal. Salt makes the soil electrically conductive by providing ions for current flow. This reduces the resistance of the earth electrode significantly.

**Funnel with Mesh:**
A funnel is placed at the top of the pipe above ground level. Water is poured through it periodically to keep the charcoal and salt moist, maintaining low earth resistance. The mesh prevents debris from blocking the funnel.

**Earth Wire:**
A GI or copper wire connects from the pipe to the metallic body of the equipment to be earthed.

**Inspection Chamber:**
A concrete chamber around the top of the pipe allows access for inspection and watering.

---

### Diagram — Pipe Earthing Cross-Section

```
Ground Level
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       [ Funnel with mesh ]
               |
       [ Inspection chamber ]
               |
       [ GI Pipe, 38mm dia ]  ←── Earth wire to equipment
               |
       ┌───────────────────┐
       │  Charcoal layer   │ ← 15 cm thick layer around pipe
       │   + Salt layer    │
       │                   │
       │  (Perforated pipe │
       │   continues down) │
       │                   │
       └───────────────────┘
               |
         (Buried ~2.5 m below ground)
```

**Labels your diagram must include:**
- GI pipe (with diameter: 38 mm)
- Burial depth (2.5 m minimum)
- Charcoal layer
- Salt layer
- Funnel with wire mesh
- Earth wire
- Inspection chamber
- Ground level line

---

### Purpose of Each Component — Quick Table

| Component | Purpose |
|---|---|
| GI Pipe | Acts as earth electrode — main current path to earth |
| Charcoal | Retains moisture, improves conductivity of surrounding soil |
| Salt | Reduces soil resistance by providing ionic conductivity |
| Funnel | For periodic watering to maintain low earth resistance |
| Wire mesh | Prevents funnel blockage |
| Earth wire | Connects equipment body to the pipe |
| Perforations in pipe | Allows moisture and ions to pass between pipe and soil |

---

### Exam Points

- Standard pipe: **GI pipe, 38 mm diameter, 2.5 m depth**
- Charcoal + salt together reduce earth resistance
- Watering must be done **periodically** (especially in summer) — if soil dries out, resistance rises and earthing becomes ineffective
- Pipe earthing is preferred over plate earthing in **rocky or sandy soil** where driving a plate deep enough is difficult
- Earth resistance must be as low as possible — ideally **less than 1 Ω** for heavy equipment

---

## 5. MCB vs ELCB vs MCCB — Quick Comparison

| Feature | MCB | ELCB / RCCB | MCCB |
|---|---|---|---|
| Full Form | Miniature Circuit Breaker | Earth Leakage / Residual Current CB | Moulded Case Circuit Breaker |
| Protects Against | Overload + Short Circuit | Earth Leakage | Overload + Short Circuit (higher ratings) |
| Rated Current Range | Up to 100 A | Typically 25–100 A | 100 A to 1600 A |
| Protects | Wiring | Humans (electric shock) | Heavy machinery, industrial panels |
| Trip Mechanism | Bimetallic + Solenoid | Core Balance CT + Relay | Thermal + Magnetic (higher capacity) |
| Resettable | Yes | Yes | Yes |
| Where Used | Domestic distribution boards | Along with MCB in DB panels | Industrial / commercial switchboards |

---

## 6. One-Line Answers — Section A Preparation

**Q: What does MCB stand for?**
Miniature Circuit Breaker — a device that automatically trips to protect a circuit from overload and short circuit.

**Q: What is the purpose of the bimetallic strip in MCB?**
It provides thermal (overload) protection by bending when it heats up due to excess current, triggering the trip mechanism.

**Q: What is ELCB and what does it detect?**
Earth Leakage Circuit Breaker — detects imbalance between live and neutral current caused by earth leakage and disconnects the circuit.

**Q: At what leakage current does ELCB trip?**
30 mA (0.03 A).

**Q: What is the minimum depth for pipe earthing?**
2.5 metres below ground.

**Q: Why is salt added in pipe earthing?**
Salt improves the electrical conductivity of the surrounding soil by reducing its resistance.

**Q: Why is XLPE preferred over PVC in industrial wiring?**
XLPE handles higher temperatures (up to 90°C vs 70°C for PVC) and has better electrical properties and longer lifespan.

**Q: What is the difference between MCB and ELCB?**
MCB protects wiring from overload and short circuit. ELCB protects humans from electric shock due to earth leakage. Both are used together in a distribution board.

---

## 7. High-Value Exam Question Formats

### 5-Mark Questions (Answer Template)

**Explain the working of MCB with diagram.**
→ Define MCB → Two mechanisms (thermal + magnetic) → Explain each → Draw labeled diagram → State when each trips

**Explain pipe earthing with diagram.**
→ Define earthing and its need → Components of pipe earthing → Draw labeled cross-section → Purpose of charcoal and salt → Maintenance requirement

**Explain ELCB with diagram.**
→ Define + purpose → Construction (CBCT, trip coil, contacts) → Normal condition → Fault condition → Trip time and leakage threshold

### 10-Mark Questions (Answer Template)

**With a neat labeled diagram, explain the construction and working of ELCB. Differentiate normal and fault conditions.**
→ Need for ELCB (2 marks) → Construction with labeled diagram (4 marks) → Normal working — balanced currents (2 marks) → Fault condition — leakage detection and trip (2 marks)

**With a neat labeled diagram, explain pipe earthing. State the purpose of each component.**
→ Need for earthing (1 mark) → Components with diagram (5 marks) → Purpose of each component (3 marks) → Maintenance and earth resistance standard (1 mark)

---

> **Final Note:** For Module 4, your diagram quality is worth more than your paragraph count. A fully labeled MCB or ELCB diagram with a clean explanation will always outscore a paragraph-heavy answer with no visual. Practise drawing each diagram at least twice before the exam.
