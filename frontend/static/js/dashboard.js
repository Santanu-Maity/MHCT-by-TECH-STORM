// ======================================
// LOGOUT
// ======================================

const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {

    logoutBtn.addEventListener("click", async () => {

        const confirmLogout = confirm(
            "Are you sure you want to logout?"
        );

        if (!confirmLogout) return;

        await fetch("/logout", {
            method: "POST"
        });

        window.location.href = "/";

    });

}


// ======================================
// LOAD DASHBOARD STATS
// ======================================

async function loadDashboard() {

    const response = await fetch("/dashboard-data");

    const data = await response.json();

    if (data.status !== "success") return;

    const dashboard = data.dashboard;

    document.getElementById("totalAssessments").textContent =
        dashboard.total_assessments;

    document.getElementById("latestState").textContent =
        dashboard.latest_state;

    document.getElementById("highestRisk").textContent =
        dashboard.highest_risk;

    document.getElementById("latestDate").textContent =
        dashboard.latest_date;

}


// ======================================
// LOAD TREND
// ======================================

async function loadTrend() {

    const response = await fetch("/trend-data");

    const data = await response.json();

    if (data.status !== "success") return;

    document.getElementById("trend").textContent =
        data.trend.trend;

    document.getElementById("trendChange").textContent =
        data.trend.change + " points";

}


// ======================================
// LOAD CHART
// ======================================

async function loadChart() {

    const response = await fetch("/chart-data");

    const data = await response.json();

    if (data.status !== "success") return;

    const chart = data.chart;

    const ctx = document
        .getElementById("mentalChart")
        .getContext("2d");

    new Chart(ctx, {

        type: "line",

        data: {

            labels: chart.labels,

            datasets: [

                {

                    label: "Mental Score",

                    data: chart.scores,

                    borderWidth: 3,

                    fill: false,

                    tension: 0.4

                }

            ]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: true

                }

            },

            scales: {

                y: {

                    beginAtZero: true,

                    max: 100

                }

            }

        }

    });

}


// ======================================
// LOAD EVERYTHING
// ======================================

loadDashboard();

loadTrend();

loadChart();