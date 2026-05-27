# Basic Electrical and Electronics Engineering
## Full Solution Set — Three Exam Papers (BTEE 101-18 / UEC101)

---

# PAPER 1 — Examination-II (05/11/2024) | 30 Marks
**Branch:** CSE/AIML/R&AI/DS | **Semester:** 1st

---

# SECTION A — 1 Mark Each

---

### Q.1(a) — 1 Mark
> *The synchronous speed of induction motor is 1500 r.p.m and rotor speed is 1440 r.p.m. Interpret slip.*

**Slip (s)** = (Ns − N) / Ns = (1500 − 1440) / 1500 = 60/1500 = **0.04 or 4%**

This means the rotor runs 4% slower than the rotating magnetic field — a typical value for a lightly loaded motor.

---

### Q.1(b) — 1 Mark
> *List the different types of cable and wires with the help of neat sketches.*

**[DIAGRAM: Cross-sections of four cable types side by side — solid single-core wire, stranded multi-core wire, coaxial cable with layers labeled (conductor, insulation, shield, jacket), and twisted pair cable with two insulated conductors twisted together]**

Types: **Solid wire**, **Stranded wire**, **Coaxial cable**, **Twisted pair cable**, and **Armoured cable (SWA)**.

---

### Q.1(c) — 1 Mark
> *What is difference between fuse and circuit breaker?*

A **fuse** is a one-time protection device — once it blows due to overcurrent, it must be replaced entirely. A **circuit breaker** (like an MCB) is reusable — it trips and can be reset by flipping the switch. A fuse is cheaper but a circuit breaker is more convenient and reliable for repeated use.

---

### Q.1(d) — 1 Mark
> *Define transducer and give an example.*

A **transducer** is a device that converts one form of energy into another — typically a physical quantity (pressure, temperature, displacement) into an electrical signal. Example: a **thermocouple** converts temperature difference into a small voltage (thermoelectric effect).

---

### Q.1(e) — 1 Mark
> *List some applications of LVDT.*

LVDT (Linear Variable Differential Transformer) is used in:
machine tool positioning, aircraft control surface measurement, civil engineering (measuring structural deflection), medical equipment (measuring blood pressure via diaphragm movement), and industrial automation for precise linear displacement feedback.

---

# SECTION B — 5 Marks Each (Both Options Solved)

---

### Q.2 — 5 Marks
> *Explain the working, principle and construction of 3 phase induction motor. Also explain torque slip characteristics of 3-phase induction motor.*

**[DIAGRAM: 3-phase induction motor cross-section with stator, rotor, air gap, squirrel cage rotor bars labeled. Separate torque-slip graph showing starting torque at s=1, peak breakdown torque, stable operating region s=0 to 0.1, and full-load torque point]**

**1. Working Principle:**
A 3-phase induction motor works on the principle of **electromagnetic induction**. When 3-phase AC supply is given to the stator winding, it produces a **Rotating Magnetic Field (RMF)** at synchronous speed. This rotating field cuts the stationary rotor conductors, inducing an EMF in them. Since the rotor conductors are short-circuited, current flows, and this current-carrying rotor sits in the stator's magnetic field — producing a **force (torque)** that makes the rotor turn, always trying to catch up with the RMF.

**2. Construction — Stator:**
The **stator** is the outer stationary part made of laminated silicon steel. It has slots on its inner surface where the 3-phase winding is placed — the three windings are displaced 120° apart electrically. When energised, they produce the RMF.

**3. Construction — Rotor:**
The most common type is the **squirrel cage rotor** — aluminium or copper bars embedded in a laminated core, short-circuited at both ends by end rings. There are no external connections to the rotor. The rotor always runs slightly slower than the RMF — this lag is called **slip**, and it is what keeps the induction process alive (if rotor matched RMF speed, no EMF would be induced).

**4. Torque-Slip Curve — Interpretation:**
- At standstill (s=1): some starting torque exists but is moderate.
- As slip decreases from 1 toward the critical slip: torque rises to its **peak (breakdown torque)**.
- Beyond the breakdown point, as slip further decreases (rotor speeds up under light load): torque decreases.
- At s=0 (synchronous speed): torque = 0. This never happens in practice.
- The **stable operating region** is s = 0 to ~0.1 — here, any load increase causes a small slip increase which produces more torque to compensate. This is self-correcting.

**5. Significance of the Curve:**
The curve tells engineers the starting torque, maximum safe load (breakdown torque), and normal operating slip range. For heavy starting loads, external methods (star-delta starter, autotransformer) are needed because starting torque from the curve alone may be insufficient.

---

### Q.2 (OR) — 5 Marks
> *The iron loss and full load copper loss of 100KVA, 6600/400 Volts single phase transformer are 600 Watts and 900 Watts. Interpret the efficiency at full load and half load at 0.8 power factor lag. Calculate the load at which maximum efficiency is obtained and its magnitude at some power factor.*

**Given:**
S = 100 kVA, Pi (Iron loss) = 600 W, Pc (Full load copper loss) = 900 W, pf = 0.8 lag

**1. Full Load Efficiency:**

Output power = S × pf = 100,000 × 0.8 = 80,000 W

η_FL = Output / (Output + Pi + Pc) × 100

η_FL = 80,000 / (80,000 + 600 + 900) × 100

**η_FL = 80,000 / 81,500 × 100 = 98.16%**

**2. Half Load Efficiency:**

At half load, copper loss scales as (load fraction)²:
Pc_half = (1/2)² × 900 = 225 W

Output at half load = (100,000/2) × 0.8 = 40,000 W

η_half = 40,000 / (40,000 + 600 + 225) × 100

**η_half = 40,000 / 40,825 × 100 = 97.98%**

**3. Load for Maximum Efficiency:**

Maximum efficiency occurs when Pi = n² × Pc

n = √(Pi / Pc) = √(600 / 900) = √(0.667) = **0.816**

So maximum efficiency load = 0.816 × 100 kVA = **81.6 kVA**

**4. Magnitude of Maximum Efficiency (at unity pf):**

At max efficiency: Pi = Pc_max = 600 W (iron loss equals copper loss)

η_max = (81,600 × 1.0) / (81,600 + 600 + 600) × 100

**η_max = 81,600 / 82,800 × 100 = 98.55%**

---

### Q.3 — 5 Marks
> *Explain any two out of MCB, ELCB and MCCB.*

**— MCB (Miniature Circuit Breaker) —**

**[DIAGRAM: MCB cross-section — input terminal, bimetallic strip, electromagnetic solenoid coil, arc chute, moving and fixed contacts, output terminal, trip lever labeled]**

**1. What MCB Does:**
An MCB automatically disconnects a circuit during overload or short circuit and can be manually reset — no fuse replacement needed. Rated for currents up to about 125A.

**2. Construction and Working:**
It has two internal protective elements: a **bimetallic strip** (for overloads) and an **electromagnetic solenoid** (for short circuits). Under sustained overload, the bimetallic strip heats, bends, and trips the mechanism — opening the contacts. Under a sudden short circuit, the massive current creates a strong magnetic field in the solenoid that instantly snaps the contacts open (within milliseconds). An **arc chute** suppresses the arc when contacts open.

**— ELCB (Earth Leakage Circuit Breaker) —**

**[DIAGRAM: ELCB showing live and neutral wires through toroidal core, sensing coil on core, relay connected to sensing coil, trip contacts in line, test button, and earth terminal labeled]**

**3. What ELCB Does:**
An ELCB detects current leaking to earth (as small as 30mA) and disconnects the supply within 30–40ms. This protects humans from electrocution — a level of protection no fuse or MCB can provide since fatal shocks occur at 50–100mA, far below any fuse's trip rating.

**4. Working Principle:**
Both live and neutral wires pass through a toroidal magnetic core. Under normal conditions, live current equals return neutral current — their fluxes cancel and the sensing coil sees zero net flux. When fault current leaks to earth, live current exceeds neutral current. The net residual flux in the core induces a voltage in the sensing coil, which triggers the relay and opens the trip contacts.

**5. Key Difference Between MCB and ELCB:**
MCB protects equipment and wiring from overloads and short circuits (reacts to high currents). ELCB protects people from electrocution by detecting earth leakage currents (reacts to tiny current imbalances). A complete electrical safety system uses both.

---

### Q.3 (OR) — 5 Marks
> *Outline the necessity of Earthing. Name the different methods of Earthing. Describe any one method of Earthing in detail.*

**[DIAGRAM: Pipe earthing cross-section — GI pipe buried vertically, alternate charcoal and salt layers around pipe, funnel with mesh at top, earth wire clamped to pipe top, ground level marked]**

**1. Necessity of Earthing:**
When a live wire accidentally touches the metallic body of equipment (a fault), that body becomes live at mains voltage. Anyone touching it completes the circuit through their body to ground — causing a fatal shock. **Earthing** provides a deliberate low-resistance path from the equipment body to the earth, so fault current flows safely into the ground instead of through a person. It also causes the protective device (fuse/MCB) to trip quickly, disconnecting power.

**2. Methods of Earthing:**
The main methods are: **Pipe Earthing**, **Plate Earthing**, **Rod Earthing**, and **Strip/Wire Earthing**. Pipe earthing is the most commonly used in domestic and industrial installations.

**3. Pipe Earthing — Construction:**
A **GI (Galvanised Iron) pipe** of about 38mm diameter and 2–2.5m length, perforated along its lower half, is buried vertically in the ground. Around the pipe, alternate layers of **charcoal and common salt (NaCl)** are packed to retain moisture and lower soil resistivity — keeping earth resistance low year-round. A **GI earth wire** is clamped to the top of the pipe and connected to all equipment frames. A mesh-covered **funnel** at the top allows periodic pouring of salt water to maintain effectiveness.

**4. How It Provides Safety:**
The pipe's perforations and the salt-charcoal mix create a large contact area with the soil. This gives a very low resistance path (typically < 1Ω) for fault current. When a fault occurs, current takes this easy path to earth instead of through a person, and the high fault current blows the fuse or trips the MCB almost instantly.

**5. Maintenance:**
Pipe earthing should be checked every few months. Salt water is poured into the funnel during dry seasons to keep resistance low. This is simpler to maintain than plate earthing which requires excavating the ground for inspection.

---

### Q.4 — 5 Marks
> *Differentiate between the Analog and Digital multimeters.*

**1. Display and Reading:**
An **Analog Multimeter (AMM)** uses a moving pointer (deflection needle) over a printed scale — the user must read the value by interpolating between scale markings. A **Digital Multimeter (DMM)** shows the measured value directly as a number on an LCD display, eliminating reading error completely.

**2. Accuracy and Resolution:**
Digital multimeters are significantly more accurate and offer higher resolution (they show values to 3–4 decimal places). Analog meters are inherently less precise due to mechanical inertia of the pointer and parallax errors when reading the scale.

**3. Input Impedance:**
DMMs have a very high input impedance (typically 10MΩ), meaning they barely disturb the circuit being measured. AMMs have lower input impedance, which can affect the circuit — especially in sensitive low-power circuits.

**4. Overload Protection and Fragility:**
Analog meters are fragile — connecting them incorrectly (wrong polarity or wrong range) can permanently damage the needle mechanism. Digital meters have built-in overload protection and auto-polarity detection, making them far more forgiving for beginners.

**5. Response to Changing Signals and Cost:**
The analog meter's continuous pointer movement makes it easier to observe trends and fluctuating readings (the needle visually "dances" with a varying signal). Digital meters can miss fast transients since they sample periodically. However, for stable precise measurements, digital is preferred. AMMs are cheaper; DMMs cost more but are standard in modern use.

---

### Q.4 (OR) — 5 Marks
> *Why do we need a transducer?*

**1. The Core Problem — Physical Quantities Are Not Electrical:**
Quantities like temperature, pressure, strain, displacement, and flow rate exist in the physical world but cannot be directly processed, displayed, or transmitted by electronic systems. Electronic systems only understand voltages and currents. A **transducer** bridges this gap by converting physical quantities into proportional electrical signals.

**2. Measurement and Monitoring:**
Without a transducer, you cannot measure most industrial and scientific quantities electronically. For example, the temperature inside a furnace cannot be wired into a control system directly — a thermocouple transducer converts that temperature into a millivoltage that the system can read and act on.

**3. Signal Transmission Over Distance:**
Electrical signals can be transmitted over long distances easily (wires, wireless). Converting a physical signal into an electrical one allows remote monitoring. A pressure sensor (transducer) at the bottom of an oil well can send a voltage signal to a control room on the surface — you cannot send the "pressure" itself.

**4. Automation and Control:**
Modern automation depends entirely on transducers as inputs to control systems. Motors, valves, heating elements — all need feedback from transducers (speed sensors, temperature sensors, flow sensors) to operate automatically. Without transducers, automated control loops cannot exist.

**5. Data Recording and Processing:**
Computers and data loggers only record electrical data. Transducers make it possible to log physical events — seismic activity, biological signals like ECG, weather conditions — in a form that can be stored, analysed, and transmitted. In short, transducers are the sensory organs of electronic systems.

---

# SECTION C — 10 Marks (Both Options Solved)

*Two sub-parts per option — assuming 5 marks each (no individual split stated).*

---

## Q.5 — Main Option

### Q.5(a) — 5 Marks
> *Illustrate the different types of batteries. Also write down the important characteristics for batteries.*

**[DIAGRAM: Side-by-side labeled diagrams of dry cell (primary) and lead-acid battery (secondary) — showing electrodes, electrolyte, terminals, and casing]**

**1. Primary Batteries (Non-Rechargeable):**
These are single-use batteries — once the chemical energy is exhausted, they are discarded. Examples:
- **Dry Cell (Leclanché Cell):** Zinc anode, carbon cathode, ammonium chloride paste electrolyte. Used in torches, clocks, TV remotes.
- **Alkaline Battery:** Zinc anode, manganese dioxide cathode, KOH electrolyte. Higher energy density and longer shelf life than standard dry cell.
- **Lithium Battery:** Very high energy density, very long shelf life. Used in cameras, medical implants, memory backup.

**2. Secondary Batteries (Rechargeable):**
These can be recharged by passing current in reverse. Examples:
- **Lead-Acid Battery:** Lead anode, lead dioxide cathode, dilute H₂SO₄ electrolyte. Used in cars, UPS systems. Heavy but cheap and reliable.
- **Lithium-Ion (Li-ion):** Lightweight, high energy density, low self-discharge. Used in phones, laptops, electric vehicles.
- **Nickel-Cadmium (NiCd):** Durable, tolerates deep discharge. Used in power tools, emergency lighting.

**3. EMF and Terminal Voltage:**
**EMF (Electromotive Force)** is the open-circuit voltage a battery can provide. **Terminal voltage** is the voltage under load — it is always lower than EMF due to internal resistance. A battery with high internal resistance gives a noticeably lower terminal voltage under load.

**4. Capacity (Ah Rating):**
Battery **capacity** is measured in Ampere-hours (Ah). A 100Ah battery can supply 100A for 1 hour, or 10A for 10 hours. This tells how long the battery can sustain a given load. Related to capacity is **energy density** — Wh/kg — how much energy fits per kilogram of battery weight.

**5. Other Key Characteristics:**
- **Cycle life:** Number of charge-discharge cycles before capacity degrades (Li-ion: ~500–1000 cycles; Lead-acid: ~300–500 cycles).
- **Self-discharge rate:** How fast a battery loses charge when sitting unused. Li-ion loses ~2% per month; NiCd can lose 10–15% per month.
- **Operating temperature range:** Batteries perform poorly in extreme cold or heat. Li-ion degrades rapidly above 60°C.

---

### Q.5(b) — 5 Marks
> *Explain any two types of transducers with example.*

**[DIAGRAM: Two separate diagrams — (1) Strain gauge bonded on a beam showing wire grid pattern and leads, Wheatstone bridge circuit alongside. (2) LVDT cross-section with primary coil, two secondary coils S1 and S2, movable iron core, AC input, and differential output labeled]**

**1. Resistive Transducer — Strain Gauge:**
A **strain gauge** works on the principle that the electrical resistance of a conductor changes when it is stretched or compressed. A fine metal wire or foil is bonded onto the surface whose strain needs to be measured. When the surface deforms under force, the gauge deforms with it — the conductor's length and cross-section change, altering its resistance. This resistance change is proportional to the strain applied.

**2. How Strain Gauge Measures:**
The resistance change is very small (typically milliohms), so it is measured using a **Wheatstone bridge circuit**, which converts the resistance change into a measurable voltage. Strain gauges are used to measure force, torque, pressure, and structural stress in bridges, aircraft, and medical devices.

**3. Inductive Transducer — LVDT:**
An **LVDT (Linear Variable Differential Transformer)** converts linear mechanical displacement into an AC voltage. It has a primary coil excited by AC and two secondary coils (S1 and S2) in series-opposition. A movable iron core links the primary to the secondaries through mutual induction.

**4. How LVDT Measures:**
At the centre (null position), coupling to both secondaries is equal — output is zero. As the core moves toward S1, VS1 increases and VS2 decreases — the differential output voltage (VS1 − VS2) is proportional to displacement. The phase of the output (in-phase or 180° out) tells the direction of movement. LVDT is highly linear, frictionless, and very precise.

**5. Comparison:**
The strain gauge is a **passive resistive transducer** — it changes resistance and needs an external bridge circuit. The LVDT is an **inductive transducer** — it produces an AC voltage output directly based on mutual inductance. Both are widely used in industrial instrumentation and measurement systems.

---

## Q.5 — OR Option

### Q.5(a) (OR) — 5 Marks
> *What is energy resource management and Explain how it is calculated by an example (elementary calculation).*

**1. What Energy Resource Management Is:**
**Energy resource management** is the process of monitoring, controlling, and optimising the use of electrical energy in a system (home, industry, or building) to reduce waste, lower costs, and maintain efficiency. It involves calculating energy consumed, identifying wasteful loads, and planning usage patterns.

**2. Basic Unit of Electrical Energy:**
Electrical energy is measured in **kilowatt-hours (kWh)**, commonly called a **unit**.
Formula: Energy (kWh) = Power (kW) × Time (hours)
Cost of energy = Units consumed × Tariff rate (₹/unit)

**3. Example Calculation — Household:**
Loads in a home:
| Appliance | Power | Hours/day | Units/day |
|-----------|-------|-----------|-----------|
| 5 LED bulbs | 5 × 10W = 50W = 0.05kW | 8 hrs | 0.4 kWh |
| Refrigerator | 150W = 0.15kW | 24 hrs | 3.6 kWh |
| TV | 100W = 0.1kW | 5 hrs | 0.5 kWh |
| Fan | 75W = 0.075kW | 12 hrs | 0.9 kWh |
| **Total** | | | **5.4 kWh/day** |

Monthly consumption = 5.4 × 30 = **162 kWh (units)**

**4. Cost Calculation:**
At a tariff of ₹6 per unit:
Monthly bill = 162 × ₹6 = **₹972**

**5. Why Management Matters:**
By switching to LED bulbs (from incandescent), setting the refrigerator to optimum temperature, and using appliances only when needed, the same household could cut consumption by 30–40%. Energy resource management quantifies exactly where the power is going — only then can waste be reduced systematically.

---

### Q.5(b) (OR) — 5 Marks
> *Explain the basic structure of LVDT and its operation.*

**[DIAGRAM: LVDT longitudinal cross-section showing cylindrical former, primary coil P at centre, secondary coils S1 and S2 symmetrically on either side, movable ferromagnetic core passing through all coils, AC excitation on primary terminals, output voltage taken across S1 and S2 in series-opposition, with null position marked]**

**1. Basic Structure:**
An LVDT consists of a hollow cylindrical former wound with three coils: one **primary coil (P)** at the centre and two **secondary coils (S1 and S2)** placed symmetrically on either side. A **movable ferromagnetic core** (usually iron alloy) slides freely inside the former without physically touching any winding. The primary is connected to an AC supply. S1 and S2 are connected in **series-opposition** (so their voltages subtract at the output).

**2. Principle — Mutual Induction:**
When AC is applied to the primary, it creates an alternating magnetic field. This field links to the secondary coils through the iron core — the amount of flux linking each secondary depends on **where the core is positioned**. The core acts as a variable flux guide, controlling how much primary flux couples to each secondary.

**3. Operation at Null Position (Core Centred):**
When the core is exactly at the centre, it links equally to S1 and S2. Both secondaries induce equal voltages. Since they are in series-opposition, Vout = VS1 − VS2 = 0V. This is the **null position** — zero output means zero displacement.

**4. Operation When Core Is Displaced:**
When the core moves toward S1: coupling with S1 increases, coupling with S2 decreases → VS1 > VS2 → Vout = VS1 − VS2 is positive and proportional to displacement. The **magnitude** of Vout gives how far the core moved (linear relationship). The **phase** of Vout compared to primary supply gives direction — toward S1 means in-phase (0°), toward S2 means 180° out of phase.

**5. Advantages of LVDT:**
No friction since the core never touches the coils — infinite mechanical life. Output is perfectly linear over a wide range. Very sensitive — can detect displacements of a few micrometres. Robust and sealed against harsh environments. Used in aerospace, machine tools, and industrial automation for precise linear position measurement.

---
---

# PAPER 2 — Examination-II (17/04/2025) | 30 Marks
**Branch:** AIDS/CSE(IoT)/ECE/CE/ME | **Semester:** 2nd

---

# SECTION A — 1 Mark Each

---

### Q.1(a) — 1 Mark
> *Illustrate the usage of ELCB.*

An **ELCB (Earth Leakage Circuit Breaker)** is used to protect people from electric shock caused by earth leakage faults. It detects any imbalance between the live and neutral currents (as small as 30mA) and disconnects the supply within 30–40ms. Used mandatorily in bathrooms, kitchens, outdoor sockets, and any location with risk of moisture contact.

---

### Q.1(b) — 1 Mark
> *Which breaker can handle higher current capacities, MCB or MCCB?*

**MCCB (Moulded Case Circuit Breaker)** handles much higher current capacities. An MCB is rated up to about **125A** and is used in domestic and small commercial circuits. An MCCB is rated from **100A up to 2500A** and is used in industrial panels, large commercial buildings, and distribution boards where high fault currents must be interrupted.

---

### Q.1(c) — 1 Mark
> *Interpret the characteristic curve of an LVDT.*

**[DIAGRAM: LVDT output voltage vs core displacement — linear graph passing through origin (null point), positive voltage for displacement in one direction, negative voltage for displacement in the other, x-axis labeled "Core Displacement (mm)", y-axis labeled "Output Voltage (V)"]**

The curve is a straight line through the origin. Zero output = null position (core centred). Voltage magnitude increases linearly with displacement. Positive and negative outputs represent opposite directions of movement.

---

### Q.1(d) — 1 Mark
> *Tell two uses of multimeter.*

1. **Voltage measurement:** Measures AC and DC voltage across components or power supply terminals.
2. **Resistance measurement:** Measures resistance of a component or checks continuity of a wire or circuit path.

(Other uses include current measurement, diode testing, and capacitance checking depending on the multimeter model.)

---

### Q.1(e) — 1 Mark
> *Demonstrate the power flow in induction motor.*

**[DIAGRAM: Power flow block diagram — Input Electrical Power (Pin) → Stator copper loss (I²R_stator) → Air gap power Pg → Rotor copper loss (s×Pg) → Mechanical power developed (1-s)×Pg → Friction & windage loss → Output shaft power (Pout)]**

Power flow: Electrical input → subtract stator losses → air gap power → subtract rotor copper loss (= slip × air gap power) → mechanical power → subtract friction/windage → shaft output.

---

# SECTION B — 5 Marks Each (Both Options Solved)

---

### Q.2 — 5 Marks
> *Illustrate the construction and working of a MCB with a labeled diagram.*

**[DIAGRAM: MCB internal cross-section — live input terminal at bottom, bimetallic strip connected in series, electromagnetic solenoid above it, moving contact arm connected to trip mechanism, fixed contact, arc chute chamber between contacts, output terminal at top, external toggle switch on side]**

**1. What an MCB Is:**
A **Miniature Circuit Breaker** is an automatic electromechanical switch that protects a circuit from overloads and short circuits. It replaces the old rewirable fuse, is resettable after tripping, and is rated for up to ~125A in domestic and commercial use.

**2. Construction — Key Components:**
Inside the moulded plastic case: a **bimetallic strip** (two metals with different thermal expansion rates bonded together), an **electromagnetic solenoid/coil**, moving and fixed **contacts**, an **arc extinguishing chamber (arc chute)**, and a manual ON/OFF toggle. All are connected in series in the circuit.

**3. Working — Overload Protection (Thermal):**
When current exceeds the rated value for a sustained period, the bimetallic strip absorbs heat and bends (because its two metals expand at different rates). As it deflects enough, it mechanically pushes the trip latch, separating the contacts and breaking the circuit. This handles gradual overloads like too many appliances on one circuit.

**4. Working — Short Circuit Protection (Magnetic):**
During a short circuit, current rises to thousands of amps almost instantly. The solenoid coil develops a powerful magnetic field in microseconds, which yanks the trip mechanism — opening contacts within one half-cycle of AC (under 10ms). The bimetallic strip would be too slow for this; the magnetic element provides the fast response.

**5. Arc Quenching and Reset:**
When contacts separate under load, an electric arc forms. The **arc chute** (a series of metal plates) divides and cools this arc rapidly, extinguishing it. Once the fault is cleared, the user flips the toggle to reset — the MCB is ready again. No parts need replacing, unlike a fuse.

---

### Q.2 (OR) — 5 Marks
> *Outline the necessity of Earthing in electrical installation. Also state different types of earthing.*

**[DIAGRAM: Simple diagram showing a fault condition — live wire touches equipment body, arrow showing fault current path through earth wire into ground, and alternative dangerous path through a person's body to ground]**

**1. Why Earthing Is Necessary — The Risk:**
In any electrical installation, insulation can degrade or wires can come loose. If a live conductor touches the metallic body of equipment (a washing machine, refrigerator, motor), that metal body becomes live at full mains voltage. A person touching it provides the path to ground and receives a potentially fatal shock. Earthing eliminates this risk.

**2. How Earthing Works:**
An **earth wire** (green or green-yellow) connects all metal equipment bodies to a buried electrode in the ground. When a fault occurs, current prefers the low-resistance earth path over the high-resistance human body. The resulting high fault current also causes the fuse or MCB to blow — disconnecting power entirely.

**3. Types of Earthing:**
- **Pipe Earthing:** GI pipe buried vertically with charcoal and salt packing. Most common for domestic use.
- **Plate Earthing:** GI or copper plate buried horizontally or vertically with charcoal and salt. Provides large contact area.
- **Rod Earthing:** Multiple GI rods driven deep into the ground. Used where ground space is limited.
- **Strip/Wire Earthing:** A bare copper strip buried horizontally in a trench. Used in large installations.
- **Water Main Earthing:** Earth electrode connected to the metallic water supply pipe (only where pipe material and continuity permits).

**4. What Earthing Protects Against:**
Protects against electric shock from faulty equipment, prevents fire due to arcing faults, protects equipment from lightning-induced surges (when combined with lightning protection), and ensures protective devices (fuses/MCBs) operate quickly by providing a low-resistance fault path.

**5. Legal Requirement:**
Earthing is not optional — it is mandatory under Indian Electricity Rules and IEC wiring standards for all buildings. Any electrical installation without proper earthing is illegal and dangerous.

---

### Q.3 — 5 Marks
> *Explain the working principle of primary and secondary transducer and provide one relevant example.*

**[DIAGRAM: Two-stage transducer block diagram — Physical Input (Pressure) → Primary Transducer (Bourdon Tube) → Mechanical Displacement → Secondary Transducer (LVDT/Potentiometer) → Electrical Output (Voltage)]**

**1. The Two-Stage Concept:**
Many physical quantities (like pressure or force) are first converted into an intermediate mechanical form, and then that mechanical output is converted into electricity. The first conversion is done by the **primary transducer** and the second by the **secondary transducer**.

**2. Primary Transducer — Definition:**
A **primary transducer** senses the original physical input and converts it into a non-electrical, usually mechanical quantity (displacement, deformation, rotation). It does not produce an electrical output directly. Its output is a physical change that can then drive a secondary transducer.

**3. Primary Transducer — Example (Bourdon Tube):**
In a pressure gauge, the **Bourdon tube** is a curved hollow tube. When fluid pressure is applied inside, the tube tends to straighten — its free end moves proportionally to the applied pressure. This tip displacement is the mechanical output of the primary transducer. The Bourdon tube has sensed pressure and converted it into displacement — but no electrical signal yet.

**4. Secondary Transducer — Definition:**
A **secondary transducer** takes the mechanical output from the primary transducer and converts it into an electrical signal (voltage or current). It is the stage that actually produces the measurable electrical output.

**5. Secondary Transducer — Example (Potentiometer or LVDT):**
The displacement of the Bourdon tube tip is connected to a **potentiometer's wiper arm** (the secondary transducer). As the tip moves, the wiper slides along the resistive track, changing the output voltage proportionally. The voltage now represents the original pressure applied. Together, Bourdon tube (primary) + potentiometer (secondary) = a complete pressure transducer system.

---

### Q.3 (OR) — 5 Marks
> *Demonstrate the construction and working of LVDT with the help of suitable neat sketch.*

**[DIAGRAM: LVDT full cross-section — hollow cylindrical former, primary coil (P) in centre connected to AC source, secondary coils (S1 left, S2 right) in series-opposition with differential output Vout labeled, movable iron core inside former, displacement arrow showing core movement direction]**

**1. Construction — Coil Assembly:**
An LVDT has a cylindrical former wound with three coils. The **primary coil (P)** sits at the centre and is excited by a fixed AC voltage (typically 1–10V, 50Hz–20kHz). The **two secondary coils (S1 and S2)** are placed symmetrically on either side of the primary. S1 and S2 are connected in **series-opposition** — meaning their induced voltages are subtracted, not added, at the output terminals.

**2. Construction — The Core:**
A **movable ferromagnetic core** (iron-nickel alloy rod) slides freely inside the former bore. It has no physical contact with any coil — this is important for frictionless, wear-free operation. The core is mechanically coupled to whatever object whose displacement is being measured.

**3. Null Position (Core Centred):**
When the core is exactly centred, it links the same amount of primary flux to both S1 and S2. Voltages induced: VS1 = VS2. Since they oppose each other, Vout = VS1 − VS2 = **0 V**. This is the null point — zero displacement, zero output.

**4. Core Displaced Toward S1:**
Mutual inductance between primary and S1 increases; between primary and S2 decreases. Now VS1 > VS2, so Vout = VS1 − VS2 is a positive AC voltage. **Magnitude** of Vout is proportional to displacement distance. **Phase** of Vout is in phase with primary supply (0°) — indicating direction toward S1.

**5. Core Displaced Toward S2:**
VS2 > VS1, output is negative (180° phase shift relative to primary). A **phase-sensitive demodulator** in the readout circuit converts this to a signed DC: positive = one direction, negative = other direction. Final output: signed DC voltage with sign = direction and magnitude = displacement amount. Highly linear, very sensitive, and ideal for precision measurement.

---

### Q.4 — 5 Marks
> *Illustrate three phase induction motor with the help of its working principle and construction.*

**[DIAGRAM: 3-phase induction motor cross-section — outer laminated stator with 3-phase winding slots (showing R, Y, B coil positions displaced 120°), inner squirrel cage rotor with aluminium bars and end rings, air gap between stator and rotor, shaft emerging from both ends]**

**1. Working Principle:**
When 3-phase AC supply is applied to the stator winding, the three currents (each 120° apart in phase) produce a **Rotating Magnetic Field (RMF)** that sweeps around the stator at **synchronous speed Ns = 120f/P**. This rotating field passes through the air gap and sweeps across the rotor conductors, **inducing an EMF** in them by Faraday's law. Since rotor conductors are short-circuited, current flows. This current in the presence of the stator's rotating magnetic field produces a **force (torque)** on the rotor — it spins, chasing the RMF.

**2. Why Slip Is Essential:**
The rotor never actually catches the RMF. If it did, there would be no relative motion, no induced EMF, no current, and no torque. The rotor always runs slightly slower — this lag is called **slip**: s = (Ns − N) / Ns. Typically 2–5% at full load.

**3. Stator Construction:**
The stator is a laminated silicon steel cylinder with slots on its inner surface. The slots carry the **3-phase winding** — three sets of coils displaced 120° apart in space. Lamination reduces eddy current losses. The stator frame provides mechanical support and is connected to the supply.

**4. Rotor Construction (Squirrel Cage Type):**
The rotor core is also laminated silicon steel. **Aluminium or copper bars** are embedded in slots on the outer surface and are **short-circuited at both ends by end-rings** — forming a cage structure. No external connections or slip rings are needed. This makes the squirrel cage motor extremely robust, cheap, and low-maintenance.

**5. Air Gap:**
A small but uniform **air gap** (0.5–2mm) separates stator and rotor. It must be kept small and uniform — a larger air gap increases the magnetising current required and reduces efficiency. The air gap is the path through which the rotating magnetic field from stator links with the rotor conductors.

---

### Q.4 (OR) — 5 Marks
> *A 220/400 V, 10 kVA, 50 Hz, single-phase transformer has copper loss of 120 W at full load. If it has an efficiency of 98% at full load, unity power factor, infer the iron losses. Infer the efficiency of the transformer at half full load at 0.8 p.f. lagging.*

**Given:**
Transformer: 220/400V, 10 kVA, 50 Hz
Full load copper loss: Pc = 120 W
Efficiency at full load, unity pf: η = 98% = 0.98

**Step 1 — Find Iron Losses (Pi):**

Full load output power = S × pf = 10,000 × 1.0 = 10,000 W

Using efficiency formula:
η = Output / (Output + Pi + Pc)
0.98 = 10,000 / (10,000 + Pi + 120)
10,000 + Pi + 120 = 10,000 / 0.98 = 10,204.08
Pi = 10,204.08 − 10,000 − 120

**Pi = 84.08 W ≈ 84 W**

**Step 2 — Efficiency at Half Load, 0.8 pf lagging:**

At half load, copper loss scales as (load fraction)²:
Pc_half = (0.5)² × 120 = 0.25 × 120 = **30 W**

Half load output = (10,000 × 0.5) × 0.8 = **4,000 W**

Iron loss remains constant at all loads: Pi = 84 W

η_half = Output / (Output + Pi + Pc_half) × 100
η_half = 4,000 / (4,000 + 84 + 30) × 100
η_half = 4,000 / 4,114 × 100

**η_half = 97.23%**

---

# SECTION C — 10 Marks

*Q.5 has two options: (a,b) together or (c,d) together. Q.5(a) and Q.5(b) are solved. Q.5(c) text is cut off in the paper — solution not attempted as question is incomplete.*

---

### Q.5(a) — 5 Marks
> *Explain wires and cables in detail.*

**[DIAGRAM: Cross-sections of five types — solid single-core, stranded multi-core, two-core PVC sheathed, coaxial cable with all layers labeled, armoured SWA cable with steel wire layer visible]**

**1. Solid (Single-Core) Wire:**
A **solid wire** consists of one thick conductor (copper or aluminium) with a PVC insulation coat. Rigid and maintains its shape. Used in fixed household wiring inside walls and conduits — where the wire will never need to flex. Easy to terminate and connect. The PVC insulation prevents contact between conductors and prevents short circuits.

**2. Stranded Wire:**
Made of multiple thin conductors twisted together and covered with PVC insulation. The twisting gives **flexibility** — the wire can bend repeatedly without breaking. Used in appliance cords, flexible connections inside control panels, automotive wiring, and any application where the wire moves during service. Stranded wire of the same cross-section rating carries the same current as solid but is far more resistant to fatigue from bending.

**3. Twin-Core and Multi-Core Cables:**
Multiple individually insulated cores are bundled inside a common outer sheath. A **twin-core cable** has a live and neutral (or two phases). A **3-core cable** adds an earth conductor. The colour coding (Brown = Live, Blue = Neutral, Green-Yellow = Earth per IEC 60446) identifies each core. Used for fixed domestic wiring, connecting switches, sockets, and appliances.

**4. Coaxial Cable:**
Has a **centre conductor**, surrounded by solid or foam insulation, then a **braided or foil metallic shield**, and an outer PVC jacket. The shield blocks external electromagnetic interference from reaching the centre conductor and also prevents the signal inside from radiating out. Used for cable TV, antenna connections, RF signal transmission, and internet (via cable modem). Frequency characteristics are defined by the cable type (RG6, RG58, etc.).

**5. Armoured Cable (SWA — Steel Wire Armoured):**
Has conductors insulated individually, then bundled inside an inner sheath, then wrapped with a layer of **galvanised steel wires**, and finally an outer PVC jacket. The steel armour provides mechanical protection against crushing, rodent attack, and accidental digging. Used for underground power distribution, outdoor installations, industrial power supply, and wherever physical damage is a risk. The armour also acts as an earth continuity conductor.

---

### Q.5(b) — 5 Marks
> *Illustrate the working principle of a transducer with a block diagram and describe any two types with examples.*

**[DIAGRAM: Transducer block diagram — Physical Quantity Input (Pressure/Force/Temperature/Displacement) → Sensing Element → Transduction Element → Signal Conditioning (Amplifier/Filter) → Electrical Output (Voltage or Current)]**

**1. Working Principle — The Block Diagram:**
A transducer's job is to convert a physical quantity into an electrical signal. The **sensing element** makes direct contact with the physical quantity being measured. The **transduction element** performs the actual energy conversion (mechanical → electrical, thermal → electrical, etc.). The **signal conditioning** block amplifies, filters, or linearises the output so it is usable by meters, data loggers, or control systems.

**2. Type 1 — Capacitive Transducer:**
A **capacitive transducer** works on the principle that capacitance C = ε₀εᵣA/d depends on the distance (d) between plates, plate area (A), or dielectric material (ε). Any physical quantity that changes one of these parameters changes the capacitance proportionally. Example: a **capacitive pressure sensor** uses a flexible diaphragm as one plate — when pressure is applied, the diaphragm deflects, changing d and therefore C. This capacitance change is converted to voltage by an oscillator circuit. Used in touch screens, microphones, and industrial pressure measurement.

**3. Why Capacitive Transducer is Useful:**
It is non-contact (no friction), has extremely fast response, very high sensitivity, and works over a wide temperature range. It requires an AC circuit to measure capacitance — DC excitation doesn't work.

**4. Type 2 — Thermoelectric Transducer (Thermocouple):**
A **thermocouple** consists of two dissimilar metal wires (e.g., iron and constantan) joined at one end (the **hot junction** — placed at the measurement point) and open at the other end (the **cold junction** or reference). The **Seebeck effect** causes a small EMF to develop proportional to the temperature difference between the hot and cold junctions. This EMF (in millivolts) is measured and converted to temperature by calibration tables.

**5. Why Thermocouple is Widely Used:**
Thermocouples can measure temperatures from −200°C to +2000°C (depending on type — Type K, Type J, Type R, etc.). They are robust, cheap, small, and require no power supply. Used in furnaces, gas burners, jet engines, and food processing where temperature must be monitored continuously and reliably.

---
---

# PAPER 3 — End Semester Exam (Fragments) | 50 Marks
**Branch:** AIDS/CSE(IoT)/ECE/CE/ME | **Semester:** 2nd | **Subject Code:** UEC101

*Note: Only fragments of this paper are available. Questions numbered as shown in the paper. Section B questions carry 4 marks each. Section C questions carry 10 marks each.*

---

# SECTION B — 4 Marks Each (Both Options Solved)

---

### Q.4 — 4 Marks
> *Solve the expression for relation between line & phase voltage in case of balanced 3 phase star connection.*

**[DIAGRAM: Phasor diagram of balanced 3-phase star system — three phase voltage phasors VR, VY, VB at 120° apart from neutral N, and line voltage phasors VRY, VYB, VBR connecting line terminals showing they are √3 times larger and 30° ahead of respective phase voltages]**

**1. Setup in Star (Y) Connection:**
In a star-connected system, all three phase windings share a common **neutral point (N)**. The voltage measured from any line terminal to neutral is the **phase voltage (Vph)**. The voltage measured between any two line terminals is the **line voltage (VL)**.

**2. Relation Between VL and Vph:**
Consider line voltage VRY (between R and Y terminals):

VRY = VRN − VYN = VR − VY (phasor subtraction)

The phase voltages VR and VY have the same magnitude (Vph) but are 120° apart.

|VRY| = |VR − VY| = √(Vph² + Vph² − 2×Vph×Vph×cos120°)

= √(Vph² + Vph² + Vph²) = √(3 × Vph²)

**VL = √3 × Vph**

**3. Current in Star Connection:**
In a star connection, each line conductor carries the current from one phase winding. There is no splitting or combining of currents at the neutral point (for balanced loads). Therefore:

**IL = Iph** (line current equals phase current)

**4. Summary:**
For a balanced 3-phase star-connected system:
- **Line voltage VL = √3 × Phase voltage Vph** (i.e., VL ≈ 1.732 × Vph)
- **Line current IL = Phase current Iph**

Example: In a 415V, 3-phase supply: Vph = 415/√3 = **240V** (standard Indian single-phase supply)

---

### Q.4 (OR) — 4 Marks
> *Solve the value of current and voltage across the load branch in the given circuit using Norton's Theorem.*
> **Circuit: 12V source, resistors 3Ω (series with source), 6Ω (shunt), 3Ω (series), RL = 1.5Ω (load)**

**[DIAGRAM: Circuit with 12V source in series with 3Ω on top rail; node A: 6Ω shunt to ground; then 3Ω in series leading to node B; RL=1.5Ω from node B to ground; terminals across RL marked A-B]**

**Step 1 — Short RL, find Norton Current (IN = ISC):**

Remove RL and short the load terminals (B to ground).
The 3Ω (right branch) now connects node A directly to ground (shorted through B).
From node A to ground: 6Ω ∥ 3Ω = (6×3)/(6+3) = **2Ω**
Total resistance seen by source = 3Ω (source series) + 2Ω = **5Ω**
Total source current = 12/5 = **2.4A**
Voltage at node A = 2.4 × 2 = **4.8V**
Norton current IN = current through the 3Ω (shorted branch) = 4.8 / 3 = **IN = 1.6A**

**Step 2 — Deactivate source, find Norton Resistance (RN):**

Short the 12V source (replace with wire).
Looking from load terminals (node B to ground):
From B: 3Ω (back to node A) in series with [6Ω ∥ 3Ω (source series resistor, now grounded)]
= 3 + (6∥3) = 3 + 2 = **RN = 5Ω**

**Step 3 — Apply Norton Equivalent, find IL and VL:**

Norton equivalent: Current source IN = 1.6A in parallel with RN = 5Ω. RL = 1.5Ω hangs across this.

IL = IN × RN / (RN + RL) = 1.6 × 5 / (5 + 1.5) = 8 / 6.5 = **IL ≈ 1.23A**

VL = IL × RL = 1.23 × 1.5 = **VL ≈ 1.85V**

---

### Q.5 — 4 Marks
> *In a 25 kVA, 2000/200 V power transformer the iron and full load copper losses are 350W and 400 W respectively. Find the efficiency at unity power factor at full load.*

**Given:**
S = 25 kVA, Vi = 2000V, V2 = 200V
Iron loss Pi = 350W, Full load copper loss Pc = 400W
Power factor = 1.0 (unity)

**Full Load Output Power:**
P_out = S × pf = 25,000 × 1.0 = **25,000 W**

**Full Load Efficiency:**
η = P_out / (P_out + Pi + Pc) × 100

η = 25,000 / (25,000 + 350 + 400) × 100

η = 25,000 / 25,750 × 100

**η = 97.09%**

---

### Q.5 (OR) — 4 Marks
> *Explain principle, construction and working of synchronous generator with suitable sketches.*

**[DIAGRAM: Synchronous generator cross-section — stationary armature (stator) on outside with 3-phase winding in slots, rotating field system (rotor) inside with field winding and DC excitation via slip rings, prime mover shaft connected to rotor]**

**1. Principle (Faraday's Law):**
A synchronous generator (alternator) works on the principle of **electromagnetic induction**. When a magnetic field rotates past stationary conductors, an alternating EMF is induced in those conductors. The frequency of this AC is directly tied to the rotor speed: f = NP/120 — making it a **synchronous** machine (output frequency is fixed by rotor speed).

**2. Construction:**
The **stator** (stationary outer part) carries the 3-phase armature winding in slots — this is where the output AC is taken from. The **rotor** (rotating inner part) carries the DC field winding excited via slip rings and brushes. When DC is supplied to the rotor winding, it becomes an electromagnet. The rotor is mechanically driven by a prime mover (steam turbine, diesel engine, water turbine).

**3. Working:**
As the rotor spins, its magnetic field sweeps past the stator conductors. Each stator coil has an alternating EMF induced in it. The three stator windings (displaced 120° in space) produce three AC EMFs displaced 120° in time — giving a balanced 3-phase output. The terminal voltage depends on field current (excitation) and can be controlled by varying DC field supply.

**4. Key Relationship:**
Output frequency f = NS × P / 120, where NS is rotor speed in rpm and P is number of poles. For 50Hz output with 2-pole rotor: NS = 3000 rpm. For 4-pole: NS = 1500 rpm. Speed must be held precisely constant to maintain fixed output frequency — hence the name "synchronous."

---

### Q.6 — 4 Marks
> *Discuss the construction of an auto-transformer and infer the expression for the copper savings in it.*

**[DIAGRAM: Auto-transformer circuit — single winding with total turns N1, input V1 across full winding, output V2 tapped from lower portion (N2 turns), common winding portion labeled, series winding portion labeled, input current I1 and output current I2 shown]**

**1. Construction:**
An **auto-transformer** has only one winding (unlike a two-winding transformer which has separate primary and secondary). This single winding is tapped at a point to give the output voltage. The portion of winding between the input and output terminal is called the **series winding**. The portion between the output terminal and neutral is the **common winding**. Both windings are electrically connected (not just magnetically) — this is the key difference from a two-winding transformer.

**2. Derivation of Copper Savings:**
Let K = N2/N1 = transformation ratio (for step-down, K < 1).

Let VA = volt-ampere rating = V1I1 = V2I2.

In a **two-winding transformer**, total copper weight ∝ I1N1 + I2N2 = VA + VA = 2VA (since I1N1 = I2N2 for ideal transformer).

In an **auto-transformer**, the series winding carries I1 with (N1−N2) turns and the common winding carries (I2−I1) with N2 turns:

Copper ∝ I1(N1−N2) + (I2−I1)N2

= I1N1 − I1N2 + I2N2 − I1N2

= (I1N1 + I2N2) − 2I1N2

= 2VA − 2VA × (N2/N1)

= **2VA(1−K)**

**3. Expression for Copper Saving:**
Copper in two-winding = 2VA
Copper in auto = 2VA(1−K)

**Copper saved = 2VA − 2VA(1−K) = 2VA × K**

As a fraction: **Copper saved / Total two-winding copper = K**

**4. Significance:**
If K = 0.9 (small voltage difference), 90% of copper is saved — the auto-transformer uses only 10% of the copper a two-winding transformer would. This makes it smaller, lighter, and cheaper for applications where galvanic isolation between primary and secondary is not required (like laboratory variacs, motor starters, and voltage stabilisers).

---

### Q.6 (OR) — 4 Marks
> *Explain principle, construction and working of single-phase induction motor with suitable sketches.*

**[DIAGRAM: Single-phase induction motor — stator with single-phase main winding and auxiliary/starting winding in slots (90° apart), squirrel cage rotor in centre, capacitor connected in series with auxiliary winding shown externally]**

**1. Principle — The Problem:**
A single-phase induction motor cannot self-start. A single-phase supply in a single winding produces a **pulsating magnetic field** (it oscillates back and forth, not rotate). By the double revolving field theory, this pulsating field is equivalent to two equal and opposite rotating magnetic fields — they produce equal and opposite torques that cancel, giving zero net starting torque.

**2. Making It Self-Starting:**
To start, a **phase difference** must be created between two winding currents — simulating a 2-phase supply. This is done by adding an **auxiliary (starting) winding** placed 90° spatially from the main winding. A capacitor in series with the auxiliary winding creates a ~90° phase difference in current. The two fluxes (90° in space and 90° in time) now produce a **rotating magnetic field** — enough to develop starting torque.

**3. Construction:**
The **stator** has two windings: the **main running winding** (thicker wire, higher inductance) and the **auxiliary starting winding** (thinner wire, with a capacitor). Both sit in stator slots, displaced 90° from each other. The **squirrel cage rotor** (same as 3-phase IM) sits inside — aluminium bars short-circuited by end rings.

**4. Working:**
At start, both windings are energised with phase-shifted currents. The rotating field drags the rotor up to speed by induction. Once the motor reaches about 75% of synchronous speed, a **centrifugal switch** (or in permanent split-capacitor types, the capacitor stays in circuit) disconnects the starting winding. The motor then runs on the main winding alone, with the rotor already spinning to maintain the induction process. Used in fans, pumps, compressors, and domestic appliances.

---

# SECTION C — 10 Marks Each (Both Options Solved)

---

### Q.7 — 10 Marks
> *Explain the construction and working of ELCB and MCB in detail.*

*10 marks with two devices — assuming 5 marks each.*

**— ELCB (Earth Leakage Circuit Breaker) — 5 Marks —**

**[DIAGRAM: ELCB cross-section — live wire and neutral wire both passing through centre of toroidal magnetic core (ring CT), sensing coil wound around the toroidal core, sensing coil output connected to relay coil, relay controls trip contacts in the live line, test button creates a bypass path from live to earth, earth terminal labeled]**

**1. Purpose of ELCB:**
An **ELCB** (also called RCD — Residual Current Device) detects earth leakage current as small as **30mA** and disconnects the supply within **30–40 milliseconds** — faster than the human heart can go into fibrillation (which requires ~100ms). It protects against electrocution in conditions where a fuse or MCB would never respond (they trip at amps, not milliamps).

**2. Construction:**
The ELCB has a **toroidal (ring-shaped) magnetic core** — a magnetic ring through which both the live and neutral wires are threaded as single-turn primary conductors. A multi-turn **sensing coil** is wound around this toroid. The sensing coil's output feeds an **electronic relay circuit** that controls the **trip contacts** (in series with the live line). A **test button** creates a deliberate tiny leakage for periodic testing.

**3. Working — Normal Condition:**
Under fault-free operation, every amp flowing out through the live wire returns through the neutral wire. |I_live| = |I_neutral|. The two conductors pass through the toroid in opposite directions — their magnetic effects are equal and opposite. Net flux in the toroid core = **zero**. The sensing coil detects nothing. Relay stays closed. Circuit operates normally.

**4. Working — Fault Condition:**
If a person touches a live conductor, some current flows through the body to ground — this current does not return through neutral. Now |I_live| > |I_neutral|. The net "residual" current is not zero. This imbalance creates a net flux in the toroidal core. The sensing coil picks up this flux, generating a small voltage that triggers the relay. The **trip contacts snap open** in under 40ms — supply is cut before a fatal shock develops.

**5. Test Button:**
The test button connects a small resistor from live to earth, creating a deliberate 30mA leakage path that bypasses the toroid. This simulates a fault — the ELCB should trip immediately. Testing monthly confirms the device works. An ELCB that doesn't trip on test must be replaced — it offers no protection.

---

**— MCB (Miniature Circuit Breaker) — 5 Marks —**

**[DIAGRAM: MCB internal cross-section — input terminal, bimetallic strip in series path, electromagnetic solenoid coil above bimetallic strip, moving contact arm linked to trip latch, fixed contact, arc chute plates between contacts, output terminal, external toggle switch indicating ON/OFF/TRIP positions]**

**6. Purpose of MCB:**
An **MCB** protects wiring and equipment from damage due to **overloads** (too many appliances) and **short circuits** (direct contact of live and neutral). Unlike a fuse, it trips and can be reset by flipping the switch — no replacement needed. Rated up to ~125A for domestic and small industrial use.

**7. Construction — Components:**
Inside the compact moulded case: a **bimetallic strip** (two dissimilar metals bonded — they expand at different rates when heated), an **electromagnetic solenoid coil** with a ferromagnetic plunger, a set of **contacts** (one moving, one fixed), an **arc extinguishing chamber** (stack of metal plates), and the external toggle switch. All are wired in series with the circuit.

**8. Overload Protection (Thermal Action):**
When current exceeds the rated value continuously (overload — e.g., 15A on a 10A circuit), the excess current heats the bimetallic strip. The differential thermal expansion causes it to **bend**. After a time delay (longer for smaller overloads, shorter for bigger ones), the bend is enough to push the trip mechanism — contacts open, circuit breaks. This is a **time-delayed inverse response**: the bigger the overload, the faster it trips.

**9. Short Circuit Protection (Magnetic Action):**
During a short circuit, current spikes to hundreds or thousands of amps within microseconds. The solenoid coil develops an enormous instantaneous magnetic force that **slams the plunger** against the trip mechanism — contacts separate in under half a cycle of AC (under 10ms). The bimetallic strip cannot react this fast — the solenoid provides instant magnetic response for fault protection.

**10. Arc Quenching and Reset:**
When contacts separate under live current, a high-energy arc forms. The **arc chute** splits the arc into many smaller arcs across multiple metal plates — each smaller arc has a higher voltage drop and is extinguished quickly. Once the fault is removed, the user pushes the toggle to reset — the spring-loaded mechanism re-engages the contacts and the MCB is ready for service again.

---

### Q.7 (OR) — 10 Marks
> *Describe the objective of earthing, and using appropriate diagrams, explain the various methods of earthing. Also write different two types of wires and cables.*

*Assumed split: Earthing objective + methods = 7 marks, Two types of wires = 3 marks.*

**[DIAGRAM: Four earthing methods side by side — (1) Pipe earthing: GI pipe vertical, charcoal+salt layers, funnel top, earth wire clamped. (2) Plate earthing: GI plate horizontal underground, charcoal+salt above and below, earth wire connected. (3) Rod earthing: multiple GI rods driven deep, connected together by strip. (4) Strip earthing: bare copper strip in horizontal trench.]**

**1. Objective of Earthing:**
The purpose of earthing (also called grounding) is to protect people and equipment by providing a **deliberate low-resistance path** from all exposed metallic parts of electrical equipment to the earth. In normal operation, no current flows through the earth wire. During a fault (live wire touching equipment body), fault current flows into the earth instead of through a person's body. The resulting high fault current also trips the protective device (fuse/MCB) — fully disconnecting power. Earthing also stabilises system voltage (prevents floating neutral) and provides a reference potential.

**2. Method 1 — Pipe Earthing:**
A **GI pipe** (38mm diameter, 2–2.5m long, perforated on lower half) is buried vertically in the ground. Alternate layers of **charcoal and common salt** are packed around it. Charcoal retains moisture; salt reduces soil resistivity. A GI earth wire is clamped to the pipe top. A funnel allows periodic salt-water treatment to maintain low resistance. Most commonly used in domestic and commercial installations. Earth resistance typically < 1Ω.

**3. Method 2 — Plate Earthing:**
A **GI plate** (60cm × 60cm × 6mm) or **copper plate** (60cm × 60cm × 3mm) is buried horizontally at a depth of at least 3 metres. The plate is surrounded by alternate layers of charcoal and salt to reduce soil resistance. The earth wire connects to the plate through a GI strip. Copper plate earthing gives lower and more stable resistance than GI but costs more. Used in large buildings and substations where the contact area with soil must be large.

**4. Method 3 — Rod Earthing:**
**Multiple GI rods** (16mm diameter, 2m long each) are driven vertically into the ground at intervals. They are interconnected by a horizontal strip conductor. This distributes the earth electrode area over a large volume of soil, achieving low overall resistance without needing a large pit to be excavated. Used where ground space is limited or soil resistivity is high (rocky terrain). Particularly common in European practice.

**5. Method 4 — Strip or Wire Earthing:**
A **bare copper or GI strip** (25mm × 1.6mm or similar) is laid horizontally in a trench about 0.5m deep, running for tens of metres. Large contact area with soil gives low resistance. Used in large industrial plants, substations, and where protection is needed across a wide area. Strips from different electrodes are bonded together to form an **earth mat** under major substations.

**6. Maintenance of All Earthing Systems:**
Earth resistance must be measured periodically (using an earth resistance tester). Resistance should be < 1Ω for good earthing. During dry seasons, all types require moisture addition (salt water). Electrode connections must be checked for corrosion. Poor earthing that has corroded can give false confidence while offering no actual protection.

**7. Two Types of Wires/Cables:**

**Solid (Single-Strand) Wire:**
A single conductor of copper or aluminium with PVC insulation. Rigid and does not flex — used for fixed wiring inside walls, conduit installations, and distribution boards. Cannot be used where repeated bending is needed as the conductor will fatigue and break. Cheaper and simpler to terminate.

**Armoured Cable (SWA — Steel Wire Armoured):**
Has individually insulated conductors inside an inner sheath, surrounded by a layer of helically wound **galvanised steel wires**, and covered by an outer PVC jacket. The steel armour resists mechanical damage — crushing, digging, rodents. Used underground, in industrial installations, for outdoor power supply runs, and anywhere mechanical damage is possible. The steel armour doubles as an earth continuity conductor, eliminating the need for a separate earth wire in many installations.

---

### Q.8 — 10 Marks
> *Explain the concept of LVDT and its working principle with the help of a clear and appropriate sketch.*

**[DIAGRAM: Full LVDT assembly — primary coil P at centre connected to AC source Vs, secondary coils S1 (left) and S2 (right) in series-opposition with output voltage Vout = VS1 − VS2 labeled, movable iron core with displacement arrow, null position marked at centre, output waveform alongside showing zero output at null, increasing positive output when core moves toward S1, increasing negative output toward S2]**

**1. What LVDT Is and Why It Is Used:**
**LVDT (Linear Variable Differential Transformer)** is a passive inductive transducer that converts **linear mechanical displacement** into a proportional **AC voltage output**. It is the most widely used linear position sensor in industrial and aerospace applications because it is frictionless (core never touches coils), has infinite resolution (no electrical contact to wear out), is highly linear, and operates reliably in harsh environments.

**2. Construction in Detail:**
The LVDT body is a hollow cylindrical former wound with three coils:
- **Primary coil (P):** Wound at the centre. Connected to an AC excitation source (typically 1–10V RMS, 50Hz to 20kHz). This creates an alternating magnetic field.
- **Secondary coil S1:** Wound to the left of the primary.
- **Secondary coil S2:** Wound to the right of the primary, identical to S1.
- S1 and S2 are connected in **series-opposition** — meaning their terminal connections are reversed, so Vout = VS1 − VS2 (subtraction, not addition).
- A **movable ferromagnetic core** (iron-nickel alloy, high permeability) slides axially inside the former bore. It is mechanically attached to the object being measured. It never contacts the windings.

**3. Working Principle — Mutual Induction:**
The primary coil's AC magnetic field links to both secondary coils through the iron core. The iron core acts as a **flux concentrator and guide** — it channels primary flux into the secondary coils. The amount of flux linking each secondary depends entirely on **how much of the core overlaps with that coil** — i.e., the core's axial position.

**4. At Null Position (Core Exactly Centred):**
The core bridges equally between S1 and S2. Primary flux links equally to both. VS1 and VS2 are induced at equal magnitude. Since they are in series-opposition: Vout = VS1 − VS2 = **0V**. This is the electrical null — zero output means zero displacement. The null is extremely precise and repeatable — a key advantage of LVDT.

**5. Core Displaced Toward S1:**
Mutual inductance between primary and S1 increases (more core overlap). Mutual inductance between primary and S2 decreases. VS1 rises, VS2 falls. Vout = VS1 − VS2 > 0. The output is a non-zero AC voltage **in phase with the primary supply (0°)**. The **magnitude** of Vout is proportional to how far the core moved from null — the relationship is highly linear over the rated range.

**6. Core Displaced Toward S2:**
VS2 > VS1. Vout = VS1 − VS2 < 0. The output is an AC voltage **180° out of phase** with the primary supply. Same magnitude relationship applies — distance from null gives magnitude, phase gives direction.

**7. How Direction Is Decoded (Phase-Sensitive Detection):**
The raw output is an AC signal — its magnitude tells displacement, its phase tells direction. A **phase-sensitive demodulator (rectifier + filter)** compares the output phase to the primary reference. In-phase signals are given a positive DC value; 180° out-of-phase signals are given a negative DC value. The final output after demodulation: **+V means displacement in one direction; −V means displacement in the other. Magnitude = distance from null.**

**8. Linearity and Range:**
The output voltage vs displacement relationship is linear over the LVDT's rated range (e.g., ±2mm, ±10mm, ±25mm depending on design). Outside this range, the output deviates from linearity. The **sensitivity** (output voltage per mm of displacement) is a key specification, typically quoted in mV/mm or V/mm.

**9. Advantages:**
Frictionless and wear-free — infinite mechanical life. No electrical contact between core and coils — no noise from contact friction. Very high resolution (limited only by signal conditioning electronics — nanometre resolution is achievable). Robust — can be fully sealed and used in oil, high pressure, or high temperature environments. Null position is absolute and repeatable — no drift.

**10. Applications:**
Used in machine tool linear position feedback, aircraft control surface position measurement, valve position control in power plants, civil engineering (monitoring bridge deflection and building settlement), medical devices (blood pressure measurement via pressure-to-displacement diaphragm), and hydraulic/pneumatic actuator position feedback in industrial automation.

---

### Q.8 (OR) — 10 Marks
> *Provide a detailed explanation of the term transducer, supported by a block diagram. Classify transducers into five distinct categories and provide a relevant example for each.*

**[DIAGRAM: Transducer block diagram — Physical Input → Sensing Element → Transduction Element → Signal Conditioning (Amplifier + Filter + ADC) → Electrical Output (Voltage / Current / Digital Signal), with feedback arrow for active transducers]**

**1. Definition of Transducer:**
A **transducer** is a device that converts one form of energy into another. In instrumentation and measurement, it specifically refers to devices that convert a **physical or chemical quantity** (mechanical, thermal, optical, chemical) into an **electrical signal** that can be processed, displayed, transmitted, or used for control. The inverse is also possible — converting electrical energy into a physical form (e.g., a loudspeaker converts electrical signals into sound). The block diagram shows: the sensing element makes contact with the measurand → the transduction element performs energy conversion → signal conditioning makes the output usable.

**2. Why Transducers Are Fundamental:**
No measurement or control system can work without transducers. Computers, meters, and controllers only understand electrical signals. Transducers are the interface that connects the physical world to electronic systems. Every sensor in a smartphone, aircraft, hospital, factory, or power plant is a transducer.

**3. Category 1 — Resistive Transducers:**
These convert the measurand into a **change in electrical resistance**.
- Principle: Physical quantity changes the conductor's geometry or material resistivity.
- Example: **Strain Gauge** — when a surface deforms under force, a bonded fine-wire grid stretches, changing its resistance proportionally to strain. Measured using a Wheatstone bridge circuit. Used for force, pressure, and torque measurement.
- Other examples: Thermistor (temperature changes resistance), potentiometer (displacement changes resistance via wiper position).

**4. Category 2 — Inductive Transducers:**
These convert the measurand into a **change in inductance or mutual inductance**.
- Principle: Changing the core position, air gap, or number of effective turns alters the coil's inductance or the mutual inductance between coils.
- Example: **LVDT (Linear Variable Differential Transformer)** — a movable iron core changes mutual inductance between a primary and two secondary coils. The differential output voltage is proportional to core displacement. Used for precise linear position measurement in machine tools, aerospace, and industrial automation.

**5. Category 3 — Capacitive Transducers:**
These convert the measurand into a **change in capacitance** (C = ε₀εᵣA/d).
- Principle: Any physical quantity that changes plate separation (d), effective plate area (A), or dielectric constant (εᵣ) changes the capacitance.
- Example: **Capacitive microphone** — sound waves cause a thin diaphragm to vibrate, changing the gap between the diaphragm and a fixed backplate. This changing capacitance, with a fixed charge (from a polarising voltage), produces a changing voltage — the audio signal. Also used in capacitive pressure sensors and touch screens.

**6. Category 4 — Piezoelectric Transducers:**
These exploit the **piezoelectric effect** — certain crystalline materials (quartz, PZT ceramics) generate an electric charge when mechanically stressed, and conversely deform when an electric field is applied.
- Principle: Mechanical stress → charge separation → measurable voltage across crystal faces.
- Example: **Quartz crystal accelerometer** — when the sensor experiences acceleration, an internal mass exerts a force on the quartz crystal. The resulting charge is proportional to the force (and thus acceleration). Used in vibration measurement, impact sensing, industrial accelerometers, and ultrasonic transducers (in sonar and medical imaging).

**7. Category 5 — Thermoelectric Transducers:**
These convert **temperature difference into an electrical voltage** using the Seebeck effect.
- Principle: When two dissimilar metals are joined at one end (hot junction) and left open at the other (cold/reference junction), a small EMF develops proportional to the temperature difference between the two junctions.
- Example: **Type K Thermocouple** (Chromel-Alumel) — can measure temperatures from −200°C to +1260°C. Widely used in furnaces, gas burners, jet engine exhausts, and any application where temperature must be sensed at a point without external power supply (thermocouples are self-generating — they need no excitation source). Output is in millivolts, read using a millivoltmeter calibrated in °C.

**8. Additional Classification Axis — Active vs Passive:**
Beyond the five categories above, transducers are also classified as:
- **Active transducers:** Generate their own electrical output without needing external power — e.g., thermocouple (generates EMF), piezoelectric sensor (generates charge), photovoltaic cell (generates voltage from light). They are self-generating.
- **Passive transducers:** Need external power/excitation to produce output — e.g., strain gauge (needs a Wheatstone bridge supply), LVDT (needs AC excitation), thermistor (needs a current source). The physical quantity modulates the electrical parameter rather than generating energy directly.

**9. Selection Criteria for a Transducer:**
Choosing the right transducer depends on: range and resolution required, operating environment (temperature, humidity, vibration), required accuracy and linearity, power availability, response time, cost, and whether galvanic isolation from the process is needed.

**10. Summary Table:**

| Category | Electrical Parameter Changed | Example | Typical Application |
|---|---|---|---|
| Resistive | Resistance (R) | Strain gauge, thermistor | Force, temperature, pressure |
| Inductive | Inductance / Mutual inductance | LVDT | Linear displacement |
| Capacitive | Capacitance (C) | Capacitive microphone | Sound, pressure, proximity |
| Piezoelectric | Charge / Voltage (self-generating) | Quartz accelerometer | Vibration, ultrasound |
| Thermoelectric | Voltage (Seebeck EMF) | Thermocouple | High-temperature measurement |

---

### Q.8(d) — Additional Fragment — 4 Marks
> *Compare analog and digital multimeters, highlighting their key differences with relevant explanations.*

**1. Display and Reading Method:**
An **Analog Multimeter (AMM)** uses a moving-coil meter movement with a **needle pointer** deflecting over a printed scale. The user estimates values by reading the pointer position — often requiring interpolation between scale markings. A **Digital Multimeter (DMM)** shows the exact measured value as a number on an **LCD display**, eliminating reading ambiguity and parallax error entirely.

**2. Accuracy and Input Impedance:**
DMMs have significantly higher accuracy (typically ±0.5% or better) and much higher input impedance (~10MΩ). High input impedance means the meter barely draws any current from the circuit under test — essential in high-impedance or sensitive circuits. AMMs have lower input impedance (5–20kΩ/V depending on range) and can load the circuit, causing measurement errors in sensitive circuits.

**3. Overload Protection and Ease of Use:**
AMMs are mechanically fragile — wrong range or reverse polarity can permanently damage the needle mechanism or meter movement. DMMs have electronic overload protection, auto-polarity detection (displays a minus sign for reversed connections), and auto-ranging (selects the correct range automatically). DMMs are far more beginner-friendly.

**4. Observation of Trends vs Precision:**
The AMM's continuous needle movement makes it **visually intuitive for observing changing or fluctuating signals** — the needle "sweeps" and the eye naturally tracks the trend. DMMs sample periodically and display a frozen number — they can miss fast transients and are harder to read on rapidly changing signals. However, for **precise stable measurements**, DMMs win on every count.

---

*— End of All Three Papers — All available questions fully solved.*
