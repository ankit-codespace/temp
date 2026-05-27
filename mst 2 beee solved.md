# UEC101T — Basic Electrical and Electronics Engineering
## Theory Examination-II | Full Solution Set

**College:** Chandigarh Engineering College, Jhanjeri, Mohali
**Semester:** 2nd | **Max Marks:** 30 | **Time:** 1.5 Hours

---

# SECTION A — 1 Mark Each

---

### Q.1(a) — 1 Mark
> *A 3-phase induction motor has 26 poles and is connected to 50 Hz AC supply. Find the synchronous speed of the RMF in the motor.*

The synchronous speed formula is **Ns = 120f / P**, where f is supply frequency and P is number of poles.

Ns = 120 × 50 / 26 = 6000 / 26 ≈ **230.77 RPM**

---

### Q.1(b) — 1 Mark
> *List the primary functions of a Miniature Circuit Breaker (MCB).*

An MCB has two primary functions — it automatically disconnects the circuit during an **overload** (excess current drawn over time) and during a **short circuit** (sudden massive current surge). It also acts as a manual ON/OFF switch for the circuit.

---

### Q.1(c) — 1 Mark
> *Infer the importance of PVC coating on wires in preventing short circuits.*

**PVC (Polyvinyl Chloride)** is an electrical insulator wrapped around the conducting wire. It prevents two live conductors from touching each other directly. If bare wires touch, current bypasses the load entirely — that is a short circuit. The PVC coating keeps conductors physically and electrically separated, preventing this.

---

### Q.1(d) — 1 Mark
> *Outline the characteristic curve of an LVDT by drawing and labeling it appropriately.*

**[DIAGRAM: LVDT output voltage vs core displacement graph, linear curve passing through zero at null position, with positive voltage for right displacement and negative for left, axes labeled "Output Voltage (V)" and "Core Displacement (mm)"]**

The curve is linear and passes through zero at the **null position** (centre). Output voltage increases proportionally as the core moves in either direction, with phase reversing to indicate direction.

---

### Q.1(e) — 1 Mark
> *Why do we need a transducer?*

Most physical quantities like temperature, pressure, or displacement cannot be directly processed or displayed by electronic systems. A **transducer** converts these physical quantities into equivalent electrical signals, which can then be measured, recorded, and transmitted easily.

---

# SECTION B — 5 Marks Each (Both Options Solved)

---

### Q.2 — 5 Marks
> *Infer the construction and working of an MCB with a labeled diagram. Describe its function in electrical safety.*

**[DIAGRAM: Labeled cross-section of MCB showing input terminal, bimetallic strip, electromagnetic coil/solenoid, arc extinguisher, trip mechanism, contacts, and output terminal]**

**1. What an MCB is:**
A **Miniature Circuit Breaker** is an automatic switching device used to protect electrical circuits from damage caused by overloads and short circuits. It replaces the older rewirable fuse and is resettable.

**2. Construction:**
The MCB has two main protective elements inside its compact housing — a **bimetallic strip** and an **electromagnetic solenoid coil**. These are connected in series with the circuit. A set of contacts (one fixed, one moving) opens or closes the circuit. An **arc chute** suppresses the arc formed when contacts open.

**3. Working under Overload (Thermal Protection):**
When current exceeds the rated value for a sustained period, the bimetallic strip heats up and bends. As it bends enough, it pushes the trip mechanism, which opens the contacts and breaks the circuit. This protects against slow, gradual overloads like too many appliances on one line.

**4. Working under Short Circuit (Magnetic Protection):**
During a short circuit, current spikes almost instantly to a very high value. The electromagnetic solenoid generates a strong magnetic field that instantly pulls the trip lever, opening the contacts within milliseconds. This is faster than the bimetallic strip can react.

**5. Role in Electrical Safety:**
Once tripped, the MCB can simply be reset by flipping the switch back — no fuse wire replacement needed. It provides reliable, repeatable protection for household and industrial circuits, preventing fire, equipment damage, and electrocution risks.

---

### Q.2 (OR) — 5 Marks
> *Explain the different types of wires used in electrical systems along with their applications.*

**1. Solid Wire (Single-Strand):**
Made of a single thick conductor, usually copper or aluminium. It is rigid, holds its shape, and is used in fixed wiring inside walls, conduit wiring, and distribution boards where the wire will not be moved or flexed.

**2. Stranded Wire:**
Made of multiple thin conductors twisted together. The flexibility makes it ideal for connections that require movement or bending — such as inside appliances, control panels, and any portable equipment. More flexible = less likely to break under vibration.

**3. Co-axial Cable:**
Has a central conductor, surrounded by insulation, then a braided metal shield, and an outer jacket. The shield blocks external interference. Used in cable TV, radio frequency signal transmission, and data communication systems.

**4. Twisted Pair Cable:**
Two insulated wires twisted around each other. Twisting cancels out electromagnetic interference picked up by each wire. Used extensively in telephone lines, LAN (Ethernet) cables, and data networks. Can be unshielded (UTP) or shielded (STP).

**5. Armoured Cable (SWA — Steel Wire Armoured):**
Has an additional layer of steel wire winding over the insulation. This gives mechanical protection against crushing, digging damage, or harsh industrial environments. Used for underground cabling, industrial power supply, and outdoor installations.

---

### Q.3 — 5 Marks
> *Outline the operating principle of an LVDT and explain the mechanism of displacement measurement.*

**[DIAGRAM: LVDT cross-section showing primary coil in centre, two secondary coils S1 and S2 on either side, movable iron core inside, AC input to primary, and differential output voltage across S1 and S2]**

**1. What LVDT Is:**
**LVDT (Linear Variable Differential Transformer)** is an electromechanical transducer that converts linear mechanical displacement into an equivalent AC voltage output. It works on the principle of mutual induction.

**2. Construction:**
It has one **primary coil** at the centre and two **secondary coils** (S1 and S2) placed symmetrically on either side. A movable **ferromagnetic core** slides freely inside these coils without contact.

**3. Operating Principle — Null Position:**
When the core sits exactly at the centre, it couples equally with both S1 and S2. The voltages induced in S1 and S2 are equal and opposite (since connected in series-opposing), so the net output is **zero volts**. This is the **null position**.

**4. Displacement Measurement — Core Moves:**
When the core moves towards S1, mutual coupling with S1 increases and with S2 decreases. So the voltage of S1 becomes greater than S2. The differential output (VS1 − VS2) is now non-zero and proportional to how far the core moved. The **magnitude** of this output gives the amount of displacement.

**5. Direction Detection:**
The output voltage is an AC signal. The **phase** of the output compared to the primary supply tells the direction — if the core moved toward S1, output is in phase with primary; if toward S2, it is 180° out of phase. So direction and magnitude both come from one output.

---

### Q.3 (OR) — 5 Marks
> *Summarize the working principle of primary and secondary transducers with one relevant example for each.*

**1. What a Transducer Does:**
A **transducer** converts a non-electrical physical quantity (like force, temperature, pressure) into an electrical signal that can be processed and measured. The conversion may happen in one step or two steps — this gives us primary and secondary transducers.

**2. Primary Transducer — Definition:**
A **primary transducer** is the first stage that senses the physical input and converts it into another non-electrical form — usually mechanical (displacement, deformation, or movement). It does not directly give an electrical output.

**3. Primary Transducer — Example:**
In a pressure measurement system, a **Bourdon tube** is a primary transducer. When pressure is applied, the tube mechanically straightens or deforms. This mechanical movement is the intermediate output — not yet electrical.

**4. Secondary Transducer — Definition:**
A **secondary transducer** takes the mechanical output of the primary transducer and converts it into an electrical signal. It is the second stage that gives the final usable output in terms of voltage or current.

**5. Secondary Transducer — Example:**
Continuing with the Bourdon tube — the mechanical displacement of the tube tip is fed to a **potentiometer** (or LVDT). This potentiometer is the secondary transducer: it converts that small mechanical movement into a proportional change in voltage, which can be read on a meter or sent to a data system.

---

### Q.4 — 5 Marks
> *Interpret the torque-slip curve of a three-phase induction motor and explain its significance.*

**[DIAGRAM: Torque vs Slip graph for 3-phase induction motor — x-axis Slip from 1 (standstill) to 0 (synchronous speed), y-axis Torque, curve starts low at s=1, rises to peak at breakdown torque, then falls to zero at s=0, with starting torque, maximum torque, and full-load torque marked]**

**1. What Slip Is:**
**Slip** is the difference between synchronous speed (Ns) and actual rotor speed (N), expressed as a fraction: s = (Ns − N) / Ns. At standstill, s = 1. At synchronous speed, s = 0 (which never actually happens in a loaded motor).

**2. Low Slip Region (Normal Operating Zone — s = 0 to ~0.1):**
In this region, torque is nearly proportional to slip. As load increases slightly, rotor slows just a bit, slip increases slightly, and torque rises to match the load. This is the **stable operating region** — the motor self-corrects when load changes.

**3. Maximum Torque — Breakdown Torque:**
As slip increases beyond a critical value, torque reaches its peak called **breakdown torque** or maximum torque. This is the highest torque the motor can deliver without stalling. If load exceeds this, the motor cannot recover.

**4. High Slip Region (s = breakdown slip to 1):**
Beyond the breakdown point, torque actually decreases as slip increases. This is the **unstable region** — if the motor enters here, it will stall completely (s → 1) unless the load is reduced. Normal operation never occurs here.

**5. Significance of the Curve:**
The torque-slip curve tells us the starting torque (at s=1), the safe operating range, the maximum load capacity, and where the motor is stable. Engineers use this to select the right motor for a given load and to design starting methods for heavy-load applications.

---

### Q.4 (OR) — 5 Marks
> *Compare the functions of different components used in the construction of a DC motor with the help of a diagram.*

**[DIAGRAM: Labeled cross-section of DC motor showing yoke/frame, field poles with field winding, armature core with armature winding, commutator, carbon brushes, and shaft]**

**1. Yoke (Outer Frame):**
The **yoke** is the outer cylindrical steel body. It provides mechanical support to the entire motor and also acts as the magnetic return path for the flux produced by the field poles. It must be made of material with high magnetic permeability.

**2. Field Poles and Field Winding:**
The **field poles** are projecting electromagnets fixed to the yoke. They carry the **field winding** (coils of wire) which, when energised with DC, produces the main magnetic flux in the motor. This flux is what the armature conductors cut to produce torque.

**3. Armature Core and Armature Winding:**
The **armature** is the rotating part. Its core is made of laminated silicon steel to reduce eddy current losses. The **armature winding** sits in slots cut into this core — these are the conductors that carry current and interact with the field flux to produce mechanical force (torque).

**4. Commutator:**
The **commutator** is a cylindrical assembly of copper segments mounted on the shaft, insulated from each other. It reverses the direction of current in the armature conductors every half rotation, ensuring that the torque always acts in the same direction — making continuous rotation possible.

**5. Brushes:**
**Carbon brushes** press against the rotating commutator and maintain electrical contact between the stationary supply circuit and the rotating armature winding. They are made of carbon to reduce wear and have good electrical conductivity. Without brushes, current cannot reach the armature.

---

# SECTION C — 10 Marks (Both Options Fully Solved)

*Two sub-parts per option — assuming 5 marks each (no individual split given in paper).*

---

## Q.5 — Main Option

### Q.5(a) — 5 Marks
> *Illustrate the construction of pipe earthing with the help of a neat labeled diagram and justifying its importance in electrical systems.*

**[DIAGRAM: Pipe earthing cross-section showing GI pipe buried vertically in ground, funnel with wire mesh at top for pouring water/salt, alternate layers of charcoal and salt around pipe, earth wire connected to pipe top via clamp, and ground level marked]**

**1. What Earthing Is:**
**Earthing** (or grounding) means connecting the metallic non-current-carrying parts of electrical equipment to the general mass of earth. Its purpose is to provide a safe path for fault current so that it flows into the earth instead of through a human body.

**2. Construction of Pipe Earthing:**
A **GI (Galvanised Iron) pipe** of about 38mm diameter and 2–2.5 metres length is used. The pipe has perforations (small holes) along its lower half to allow moisture and current to spread into surrounding soil. The pipe is buried vertically in the ground.

**3. The Fill Material:**
Around the buried pipe, alternate layers of **charcoal and common salt (NaCl)** are packed. Charcoal retains moisture and salt lowers the resistivity of the surrounding soil. Together, they ensure low and stable earth resistance throughout seasons, even in dry conditions.

**4. Surface Connection and Maintenance:**
At the top of the pipe (just above ground level), a **GI wire or strip** is clamped securely and run to the equipment to be earthed. A funnel with a mesh cover is also provided at the top — this is for periodically pouring **salt water** into the pipe to keep the soil moist and resistance low.

**5. Importance in Electrical Safety:**
Pipe earthing provides a reliable low-resistance path to ground. If a live wire accidentally touches the metallic body of equipment (a fault), the fault current immediately flows through the earth wire into the pipe and into the ground — instead of waiting for a human to complete the path. This either trips the MCB/fuse (safely disconnecting power) or at minimum keeps the touch voltage at a safe level, preventing electrocution, fire, and equipment damage.

---

### Q.5(b) — 5 Marks
> *Demonstrate the working of a transducer using a neat block diagram and illustrate any two types of transducers with suitable examples.*

**[DIAGRAM: Block diagram showing Physical Input (pressure/temp/displacement) → Sensing Element → Signal Conditioning → Electrical Output (voltage/current), with labels at each block]**

**1. What a Transducer Does:**
A **transducer** senses a physical quantity and converts it into a proportional electrical signal. The core idea is: physical world in → electrical signal out. This makes measurement, display, and control of physical quantities possible using electronic systems.

**2. Working (from block diagram):**
The **sensing element** directly contacts or responds to the physical input. Its output (which may be mechanical) goes to the **signal conditioning** stage, which converts and amplifies it into a clean, usable electrical output — voltage or current — that instruments can read.

**3. Type 1 — Resistive Transducer (example: Strain Gauge):**
A **strain gauge** is a fine wire or foil pattern bonded to a surface. When the surface is stressed or deformed, the wire stretches or compresses, changing its resistance. This resistance change is proportional to the strain (deformation). By measuring the resistance change using a Wheatstone bridge circuit, strain — and hence force or pressure — is accurately measured.

**4. Type 2 — Inductive Transducer (example: LVDT):**
An **LVDT (Linear Variable Differential Transformer)** converts linear displacement into a voltage. A movable iron core inside the coil assembly changes the mutual inductance between primary and secondary coils as it moves. The resulting differential voltage output is proportional to displacement. Used to measure small mechanical movements very precisely.

**5. Why Transducers Are Essential:**
Without transducers, quantities like temperature, pressure, and displacement are just invisible physical phenomena. Transducers are the bridge between the physical world and electronic measurement — they are the first and most critical component in any instrumentation or control system.

---

## Q.5 — OR Option

### Q.5(c) — 5 Marks
> *Show the construction of an ELCB using a neat labeled diagram and explain its functioning under normal and faulty conditions.*

**[DIAGRAM: ELCB diagram showing live wire and neutral wire passing through a toroidal (ring) core/CT, sensing coil wound on core, relay/trip coil connected to sensing coil, contacts in series with live wire, test button, and earth connection point, with labels]**

**1. What an ELCB Is:**
An **ELCB (Earth Leakage Circuit Breaker)**, also called an RCD (Residual Current Device), is a safety device that detects small leakage currents flowing to earth and instantly disconnects the supply. It protects humans from electrocution even when current leakage is too small to blow a fuse.

**2. Construction:**
The ELCB has a **toroidal (ring-shaped) magnetic core** through which both the live and neutral wires pass as primary conductors. A **sensing coil** is wound around this core. The sensing coil is connected to an **electronic relay** which controls the **trip contacts** in series with the circuit. A **test button** creates a small artificial imbalance to verify operation.

**3. Working under Normal Conditions:**
Under normal (fault-free) conditions, current flowing through the live wire to the load returns completely through the neutral wire. Live current = Neutral current. The magnetic fluxes they produce in the toroidal core are equal and opposite — they cancel out perfectly. Net flux = zero. The sensing coil produces no output. The relay stays closed. Circuit operates normally.

**4. Working under Faulty Conditions:**
If a person touches a live conductor or insulation fails, some current flows to earth through the fault path instead of returning via neutral. Now live current > neutral current. The fluxes no longer cancel — a net residual flux appears in the core. The sensing coil picks this up, generates a small voltage, which triggers the relay. The trip contacts open within 30–40 milliseconds — fast enough to prevent a fatal shock (threshold is typically 30mA).

**5. Advantage over MCB/Fuse:**
A fuse or MCB trips only at large currents (amps). A fatal shock can occur at just 50–100mA — far below any fuse rating. The ELCB detects leakage as small as **30mA** and disconnects in under 40ms, providing protection that no fuse or MCB can offer. It is mandatory in bathrooms, kitchens, and outdoor circuits.

---

### Q.5(d) — 5 Marks
> *Contrast the working of an LVDT in displacement measurement, highlighting the way phase difference represents direction and magnitude.*

**[DIAGRAM: LVDT output waveform diagram showing: core at null position giving zero output; core displaced left giving output in phase with primary; core displaced right giving output 180° out of phase with primary; magnitude of output proportional to distance from null]**

**1. Recap of LVDT Structure:**
The **LVDT** has a primary coil (AC excited) at the centre and two secondary coils S1 and S2 placed symmetrically, connected in **series-opposition** (their voltages subtract). A movable iron core inside controls how much flux links each secondary.

**2. At Null Position — Zero Output:**
When the core is exactly centred, mutual coupling to S1 and S2 is identical. VS1 = VS2. Since they are connected in series-opposition, Vout = VS1 − VS2 = 0V. This is called the **null position** and represents zero displacement.

**3. Magnitude of Displacement:**
When the core moves away from centre (in either direction), one secondary gets more coupling and the other gets less. The difference |VS1 − VS2| increases proportionally with how far the core moved. So the **magnitude of the output voltage directly indicates how much displacement occurred**. The relationship is linear over the working range.

**4. Direction — How Phase Difference Works:**
The direction of movement cannot be told from magnitude alone (moving 5mm left and 5mm right both give the same voltage magnitude). The **phase** resolves this. When the core moves toward S1, VS1 > VS2 and the output is **in phase** with the primary supply (0°). When the core moves toward S2, VS2 > VS1 and the output is **180° out of phase** with the primary. A phase-sensitive detector (demodulator) in the readout circuit checks this phase and converts it to a positive or negative DC signal indicating direction.

**5. Combined Reading:**
The final output after demodulation is a signed DC voltage — the **sign (+ or −) tells direction**, the **magnitude tells displacement amount**. For example, +3V might mean 3mm displacement to the right and −3V means 3mm to the left. This makes the LVDT a complete displacement sensor that gives both magnitude and direction from a single output, making it extremely useful in precision engineering, machine tools, and aerospace applications.

---

*— End of Paper — All questions from Section A, B, and C (both options) have been solved.*
