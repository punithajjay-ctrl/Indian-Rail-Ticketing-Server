import streamlit as st
import plotly.graph_objects as go
import random
import struct
from collections import OrderedDict

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Indian Rail Ticketing Server",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

COLORS = [
    "#00D4FF", "#00E676", "#FFB300",
    "#FF4081", "#9C6BFF", "#FF7043"
]

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #071426, #10243a);
    color: white;
}

.block-container {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] {
    background: #0b1c30;
}

[data-testid="stSidebar"] * {
    color: white;
}

.hero {
    background: linear-gradient(120deg, #10243a, #075985, #176b87);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px #00000055;
    animation: slideIn 1s ease;
}

.hero h1 {
    color: white;
    font-size: 34px;
}

.hero p {
    color: #d7efff;
    font-size: 16px;
}

.metric-card {
    background: linear-gradient(135deg, #142d49, #1b4263);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #28658c;
    min-height: 115px;
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 18px #00d4ff55;
}

.metric-label {
    color: #a9c9e2;
    font-size: 14px;
}

.metric-value {
    color: #00e5ff;
    font-size: 27px;
    font-weight: bold;
}

.module-card {
    background: linear-gradient(135deg, #142d49, #1b4263);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #28658c;
    min-height: 150px;
    margin-bottom: 15px;
    transition: 0.3s;
}

.module-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 18px #00d4ff55;
}

.module-card h4 {
    color: #00e5ff;
}

.module-card p {
    color: #c5d9e9;
}

h1, h2, h3 {
    color: white;
}

.stButton button {
    background: linear-gradient(90deg, #0077b6, #00b4d8);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================
# SESSION STATE
# =====================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "simulations" not in st.session_state:
    st.session_state.simulations = 0

if "last_results" not in st.session_state:
    st.session_state.last_results = {}


# =====================================
# GRAPH FUNCTION
# =====================================

def show_bar_chart(title, labels, values, y_title="Count"):

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        marker_color=COLORS[:len(labels)],
        text=values,
        textposition="outside",
        hovertemplate="%{x}<br>Value: %{y}<extra></extra>"
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Category",
        yaxis_title=y_title,
        template="plotly_dark",
        paper_bgcolor="#10243a",
        plot_bgcolor="#10243a",
        font=dict(color="white"),
        height=400,
        transition_duration=700
    )

    st.plotly_chart(fig, use_container_width=True)


def show_animated_chart():

    labels = [
        "Booking", "Cancellation",
        "Enquiry", "Payment", "PNR"
    ]

    fig = go.Figure(
        data=[go.Bar(
            x=labels,
            y=[10, 5, 8, 7, 6],
            marker_color=COLORS[:5]
        )]
    )

    frames = []

    for step in range(1, 6):
        frames.append(go.Frame(
            data=[go.Bar(
                x=labels,
                y=[
                    10 * step,
                    5 * step,
                    8 * step,
                    7 * step,
                    6 * step
                ],
                marker_color=COLORS[:5]
            )],
            name=str(step)
        ))

    fig.frames = frames

    fig.update_layout(
        title="Animated Railway Server Workload",
        template="plotly_dark",
        paper_bgcolor="#10243a",
        plot_bgcolor="#10243a",
        font=dict(color="white"),
        height=420,
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {
                    "label": "▶ Play Animation",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": 700, "redraw": True},
                        "transition": {"duration": 400},
                        "fromcurrent": True
                    }]
                },
                {
                    "label": "⏸ Pause",
                    "method": "animate",
                    "args": [[None], {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate"
                    }]
                }
            ]
        }]
    )

    st.plotly_chart(fig, use_container_width=True)


def metric_card(label, value):

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


# =====================================
# SIDEBAR
# =====================================

pages = [
    "Dashboard",
    "Workload Generator",
    "Cache Memory",
    "Virtual Memory & TLB",
    "IEEE 754 Fare Calculator",
    "I/O & DMA Simulation",
    "Performance Evaluation"
]

st.sidebar.title("🚆 RAIL SERVER")
st.sidebar.caption("COA Simulation Project")
st.sidebar.markdown("---")

selected_page = st.sidebar.radio(
    "MAIN MENU",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = selected_page

st.sidebar.markdown("---")

st.sidebar.info(
    "Indian Rail Ticketing Server\n\n"
    "Computer Organization and Architecture Simulation"
)

st.sidebar.caption("Project Version 2.0")


# =====================================
# HEADER - CORRECTED HTML
# =====================================

st.markdown("""
<div class="hero">
    <h1>🚆 Indian Rail Ticketing Server</h1>
    <p>Computer Organization and Architecture Based Railway Reservation Server Simulator</p>
    <p>Workload | Cache Memory | Virtual Memory | IEEE 754 | I/O &amp; DMA | Performance</p>
</div>
""", unsafe_allow_html=True)


# =====================================
# DASHBOARD
# =====================================

if selected_page == "Dashboard":

    st.subheader("📊 System Dashboard")

    st.write(
        "Welcome to the Indian Rail Ticketing Server Simulation Platform."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Total Modules", "06")

    with c2:
        metric_card("Simulations Run", st.session_state.simulations)

    with c3:
        metric_card("Server Status", "ONLINE")

    with c4:
        metric_card("Version", "2.0")

    st.markdown("---")
    st.subheader("🧩 Simulation Modules")

    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div class="module-card">
            <h4>1. Workload Generator</h4>
            <p>Generate railway booking, cancellation, enquiry and payment requests.</p>
        </div>
        <div class="module-card">
            <h4>2. Cache Memory</h4>
            <p>Study cache hits, misses, hit ratio and memory access.</p>
        </div>
        <div class="module-card">
            <h4>3. Virtual Memory &amp; TLB</h4>
            <p>Study page replacement, page faults and address translation.</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="module-card">
            <h4>4. IEEE 754 Fare Calculator</h4>
            <p>Calculate ticket fares and demonstrate floating-point representation.</p>
        </div>
        <div class="module-card">
            <h4>5. I/O &amp; DMA Simulation</h4>
            <p>Compare CPU-controlled I/O and DMA transfer.</p>
        </div>
        <div class="module-card">
            <h4>6. Performance Evaluation</h4>
            <p>Analyze server performance using graphs and statistics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🌈 Live Animated Workload Graph")

    show_animated_chart()

    st.caption("Demonstration values only. Not live railway server data.")


# =====================================
# WORKLOAD GENERATOR
# =====================================

elif selected_page == "Workload Generator":

    st.subheader("🚆 Railway Workload Generator")

    total = st.slider("Number of requests", 10, 500, 100)

    if st.button("🚀 Generate Workload"):

        types = [
            "Booking", "Cancellation",
            "Enquiry", "Payment", "PNR Check"
        ]

        values = [random.randint(10, total) for _ in types]

        st.session_state.last_results["workload"] = dict(
            zip(types, values)
        )

        st.session_state.simulations += 1

    result = st.session_state.last_results.get("workload")

    if result:
        values = list(result.values())

        a, b, c = st.columns(3)

        with a:
            metric_card("Total Requests", sum(values))

        with b:
            metric_card("Request Types", len(values))

        with c:
            metric_card("Largest Workload", max(values))

        show_bar_chart(
            "Railway Request Distribution",
            list(result.keys()),
            values,
            "Number of Requests"
        )


# =====================================
# CACHE MEMORY
# =====================================

elif selected_page == "Cache Memory":

    st.subheader("⚡ Cache Memory Simulation")

    cache_size = st.slider("Cache Size", 2, 10, 3)

    sequence_text = st.text_input(
        "Memory Access Sequence",
        "1,2,3,1,4,2,5,1,2,3"
    )

    if st.button("▶ Run Cache Simulation"):

        try:
            sequence = [
                int(x.strip())
                for x in sequence_text.split(",")
            ]

            if not sequence:
                raise ValueError

            cache = OrderedDict()
            hits = 0
            misses = 0

            for page in sequence:

                if page in cache:
                    hits += 1
                    cache.move_to_end(page)

                else:
                    misses += 1

                    if len(cache) >= cache_size:
                        cache.popitem(last=False)

                    cache[page] = True

            hit_ratio = hits / len(sequence) * 100

            st.session_state.last_results["cache"] = {
                "hits": hits,
                "misses": misses,
                "ratio": hit_ratio
            }

            st.session_state.simulations += 1

        except ValueError:
            st.error("Enter valid numbers separated by commas.")

    result = st.session_state.last_results.get("cache")

    if result:

        a, b, c = st.columns(3)

        with a:
            metric_card("Cache Hits", result["hits"])

        with b:
            metric_card("Cache Misses", result["misses"])

        with c:
            metric_card("Hit Ratio", f'{result["ratio"]:.2f}%')

        show_bar_chart(
            "Cache Hits vs Misses",
            ["Hits", "Misses"],
            [result["hits"], result["misses"]],
            "Access Count"
        )


# =====================================
# VIRTUAL MEMORY
# =====================================

elif selected_page == "Virtual Memory & TLB":

    st.subheader("💾 Virtual Memory & TLB Simulation")

    frames = st.slider("Number of Memory Frames", 2, 8, 3)

    reference_text = st.text_input(
        "Page Reference Sequence",
        "1,2,3,4,1,2,5,1,2,3,4,5"
    )

    if st.button("▶ Run Virtual Memory"):

        try:
            pages = [
                int(x.strip())
                for x in reference_text.split(",")
            ]

            if not pages:
                raise ValueError

            memory = []
            hits = 0
            faults = 0

            for page in pages:

                if page in memory:
                    hits += 1

                else:
                    faults += 1

                    if len(memory) < frames:
                        memory.append(page)

                    else:
                        memory.pop(0)
                        memory.append(page)

            st.session_state.last_results["virtual"] = {
                "hits": hits,
                "faults": faults,
                "tlb": hits
            }

            st.session_state.simulations += 1

        except ValueError:
            st.error("Enter valid page numbers separated by commas.")

    result = st.session_state.last_results.get("virtual")

    if result:

        a, b, c = st.columns(3)

        with a:
            metric_card("Memory Hits", result["hits"])

        with b:
            metric_card("Page Faults", result["faults"])

        with c:
            metric_card("TLB Hits (Simplified)", result["tlb"])

        show_bar_chart(
            "Virtual Memory Performance",
            ["Memory Hits", "Page Faults", "TLB Hits"],
            [result["hits"], result["faults"], result["tlb"]],
            "Count"
        )

        st.info(
            "Educational FIFO page replacement model. "
            "TLB hits are simplified approximations."
        )


# =====================================
# IEEE 754 FARE CALCULATOR
# =====================================

elif selected_page == "IEEE 754 Fare Calculator":

    st.subheader("💰 IEEE 754 Fare Calculator")

    fare = st.number_input(
        "Ticket Fare per Passenger (₹)",
        min_value=1.0,
        value=250.0
    )

    passengers = st.number_input(
        "Number of Passengers",
        min_value=1,
        max_value=100,
        value=2
    )

    discount = st.slider(
        "Discount Percentage",
        0, 50, 10
    )

    if st.button("🧮 Calculate Fare"):

        subtotal = fare * passengers
        discount_amount = subtotal * discount / 100
        total = subtotal - discount_amount

        packed = struct.pack("!f", float(total))

        binary = format(
            struct.unpack("!I", packed)[0],
            "032b"
        )

        st.session_state.last_results["fare"] = {
            "subtotal": subtotal,
            "discount": discount_amount,
            "total": total,
            "binary": binary
        }

        st.session_state.simulations += 1

    result = st.session_state.last_results.get("fare")

    if result:

        a, b, c = st.columns(3)

        with a:
            metric_card("Subtotal", f'₹{result["subtotal"]:.2f}')

        with b:
            metric_card("Discount", f'₹{result["discount"]:.2f}')

        with c:
            metric_card("Final Fare", f'₹{result["total"]:.2f}')

        st.markdown("### IEEE 754 Single Precision")

        st.code(result["binary"])

        st.write("Sign bit:", result["binary"][0])
        st.write("Exponent:", result["binary"][1:9])
        st.write("Mantissa:", result["binary"][9:])

        show_bar_chart(
            "Fare Calculation",
            ["Subtotal", "Discount", "Final Fare"],
            [
                result["subtotal"],
                result["discount"],
                result["total"]
            ],
            "Amount in Rupees"
        )


# =====================================
# I/O & DMA
# =====================================

elif selected_page == "I/O & DMA Simulation":

    st.subheader("🔄 I/O and DMA Simulation")

    st.write("Compare CPU-controlled transfer with DMA transfer.")

    data_size = st.slider(
        "Data Transfer Size (MB)",
        10, 1000, 100
    )

    if st.button("▶ Run I/O Simulation"):

        cpu_time = data_size / 10
        dma_time = data_size / 40

        improvement = (
            (cpu_time - dma_time) / cpu_time
        ) * 100

        st.session_state.last_results["io"] = {
            "cpu": cpu_time,
            "dma": dma_time,
            "improvement": improvement
        }

        st.session_state.simulations += 1

    result = st.session_state.last_results.get("io")

    if result:

        a, b, c = st.columns(3)

        with a:
            metric_card("CPU Transfer", f'{result["cpu"]:.2f} s')

        with b:
            metric_card("DMA Transfer", f'{result["dma"]:.2f} s')

        with c:
            metric_card("Time Reduction", f'{result["improvement"]:.1f}%')

        show_bar_chart(
            "CPU vs DMA Transfer Time",
            ["CPU I/O", "DMA"],
            [result["cpu"], result["dma"]],
            "Time in Seconds"
        )

        st.success(
            "DMA reduces the illustrative transfer time."
        )

        st.caption(
            "Educational estimate using assumed transfer speeds."
        )


# =====================================
# PERFORMANCE EVALUATION
# =====================================

elif selected_page == "Performance Evaluation":

    st.subheader("📈 Server Performance Evaluation")

    if st.button("▶ Generate Performance Report"):

        operations = [
            "Booking", "Payment",
            "Cancellation", "Enquiry", "PNR Check"
        ]

        response = [
            random.randint(20, 100)
            for _ in operations
        ]

        st.session_state.last_results["performance"] = {
            "operations": operations,
            "response": response
        }

        st.session_state.simulations += 1

    result = st.session_state.last_results.get("performance")

    if result:

        average = sum(result["response"]) / len(result["response"])

        a, b = st.columns(2)

        with a:
            metric_card("Average Response", f"{average:.2f} ms")

        with b:
            metric_card("Operations Tested", len(result["operations"]))

        show_bar_chart(
            "Server Response Time",
            result["operations"],
            result["response"],
            "Response Time (ms)"
        )

        if average < 50:
            st.success("Excellent simulated response time.")

        elif average < 75:
            st.warning("Moderate simulated response time.")

        else:
            st.error("High simulated response time.")


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown("""
<div style="text-align:center; color:#9bbbd2;">
    Indian Rail Ticketing Server Simulator<br>
    Python + Streamlit + Plotly | COA Project
</div>
""", unsafe_allow_html=True)