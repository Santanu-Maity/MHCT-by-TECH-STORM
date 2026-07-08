console.log("assessment.js loaded");
// ======================================
// MENTAL HEALTH ASSESSMENT QUESTIONS
// ======================================

const questions = [

    {
        key: "age",
        question: "What is your age?",
        type: "number",
        placeholder: "Enter your age"
    },

    {
        key: "gender",
        question: "What is your gender?",
        type: "radio",
        options: [
            "Male",
            "Female",
            "Other"
        ]
    },

    {
        key: "employment_status",
        question: "Employment Status",
        type: "radio",
        options: [
            "Student",
            "Employed",
            "Unemployed"
        ]
    },

    {
        key: "relationship_status",
        question: "Relationship Status",
        type: "radio",
        options: [
            "Single",
            "Married",
            "Relationship"
        ]
    },

    {
        key: "sleep_hours",
        question: "Average Sleep Hours",
        type: "number",
        placeholder: "Example: 7"
    },

    {
        key: "sleep_quality",
        question: "Rate your sleep quality (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "food_quality",
        question: "Rate your food quality (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "water_intake",
        question: "Water intake (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "exercise_hours",
        question: "Exercise hours per day",
        type: "number",
        placeholder: "Example: 1"
    },

    {
        key: "screen_time",
        question: "Screen time per day (hours)",
        type: "number",
        placeholder: "Example: 6"
    },

    {
        key: "hobbies_time",
        question: "Hobbies time per day (hours)",
        type: "number",
        placeholder: "Example: 2"
    },

    {
        key: "work_stress",
        question: "Work stress (1-10)",
        type: "number",
        placeholder: "1 to 10"
    },

    {
        key: "academic_pressure",
        question: "Academic pressure (1-10)",
        type: "number",
        placeholder: "1 to 10"
    },

    {
        key: "financial_stress",
        question: "Financial stress (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "social_interaction",
        question: "Social interaction (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "family_support",
        question: "Family support (1-5)",
        type: "number",
        placeholder: "1 to 5"
    },

    {
        key: "daily_productivity",
        question: "Daily productivity (1-10)",
        type: "number",
        placeholder: "1 to 10"
    },

    {
        key: "health_issues",
        question: "Any health issues?",
        type: "radio",
        options: [
            {
                label: "No",
                value: 0
            },
            {
                label: "Yes",
                value: 1
            }
        ]
    }

];

let currentQuestion = 0;
const answers = {};
// ======================================
// DOM ELEMENTS
// ======================================

const questionContainer = document.getElementById("questionContainer");
const progressBar = document.getElementById("progressBar");

const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");

const resultContainer = document.getElementById("resultContainer");
const toast = document.getElementById("toast");
const loadingContainer = document.getElementById("loadingContainer");


// ======================================
// SHOW QUESTION
// ======================================

function showQuestion() {

    const q = questions[currentQuestion];

    progressBar.style.width =
        ((currentQuestion + 1) / questions.length) * 100 + "%";

    let html = `
        <h2 class="question">
            Question ${currentQuestion + 1} of ${questions.length}
        </h2>

        <h3 style="margin-bottom:25px;">
            ${q.question}
        </h3>
    `;

    if (q.type === "number") {

        html += `
            <input
                class="text-input"
                id="answer"
                type="number"
                placeholder="${q.placeholder}"
                value="${answers[q.key] ?? ""}"
            >
        `;

    }

    else if (q.type === "radio") {

        html += `<div class="options">`;

        q.options.forEach(option => {

            let value;
            let label;

            if (typeof option === "object") {

                value = option.value;
                label = option.label;

            } else {

                value = option;
                label = option;

            }

            html += `
                <label class="option">

                    <input
                        type="radio"
                        name="answer"
                        value="${value}"

                        ${
                            answers[q.key] == value
                            ? "checked"
                            : ""
                        }
                    >

                    <span>${label}</span>

                </label>
            `;

        });

        html += `</div>`;

    }

    questionContainer.innerHTML = html;

    prevBtn.style.display =
        currentQuestion === 0
            ? "none"
            : "inline-block";

    nextBtn.style.display =
        currentQuestion === questions.length - 1
            ? "none"
            : "inline-block";

    submitBtn.style.display =
        currentQuestion === questions.length - 1
            ? "inline-block"
            : "none";

}
// ======================================
// SAVE CURRENT ANSWER
// ======================================

function saveAnswer() {

    const q = questions[currentQuestion];

    if (q.type === "number") {

        const input = document.getElementById("answer");

        if (!input.value) {

            showToast("Please enter a value.");

            return false;

        }

        answers[q.key] = Number(input.value);

    }

    else {

    const selected = document.querySelector(
        'input[name="answer"]:checked'
    );

    if (!selected) {

        showToast("Please select an option.");
        return false;

    }

    // These fields MUST remain strings
    if (
        q.key === "gender" ||
        q.key === "employment_status" ||
        q.key === "relationship_status"
    ) {

        answers[q.key] = selected.value;

    }

    // health_issues is numeric (0 or 1)
    else {

        answers[q.key] = Number(selected.value);

    }

}
    return true;

}


// ======================================
// NEXT BUTTON
// ======================================

nextBtn.addEventListener("click", () => {

    if (!saveAnswer()) return;

    currentQuestion++;

    showQuestion();

});


// ======================================
// PREVIOUS BUTTON
// ======================================

prevBtn.addEventListener("click", () => {

    currentQuestion--;

    showQuestion();

});
// ======================================
// SUBMIT ASSESSMENT
// ======================================

submitBtn.addEventListener("click", async () => {

    if (!saveAnswer()) return;

    submitBtn.disabled = true;
    submitBtn.innerText = "Analyzing...";

    // Hide assessment

questionContainer.style.display = "none";
document.querySelector(".navigation-buttons").style.display = "none";

// Show loading spinner

loadingContainer.style.display = "block";

    try {

        console.log("Sending Data:", answers);

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(answers)

        });

        const result = await response.json();

        if (result.status === "success") {

            questionContainer.style.display = "none";
            document.querySelector(".navigation-buttons").style.display = "none";

            loadingContainer.style.display = "none";

            resultContainer.style.display = "block";

            let riskClass = "low";

if (result.risk_level.toLowerCase().includes("medium")) {
    riskClass = "medium";
}

if (result.risk_level.toLowerCase().includes("high")) {
    riskClass = "high";
}

resultContainer.innerHTML = `

<div class="result-card">

    <h2 style="text-align:center;">
        🧠 Assessment Complete
    </h2>

    <div class="result-item">
        <strong>Mental State:</strong>
        ${result.mental_state}
    </div>

    <div class="result-item">
        <strong>Mental Score:</strong>
        ${result.mental_score}/100
    </div>

    <div class="result-item">
        <strong>Anxiety Score:</strong>
        ${result.anxiety_score}
    </div>

    <div class="result-item">
        <strong>Depression Score:</strong>
        ${result.depression_score}
    </div>

    <div class="result-item">
        <strong>Risk Level:</strong>

        <span class="${riskClass}">
            ${result.risk_level}
        </span>

    </div>

    <hr style="margin:20px 0;">

    <div class="result-item">

        <strong>AI Recommendation</strong>

        <br><br>

        ${result.recommendation}

    </div>

    <div class="result-buttons">

        <button id="newAssessmentBtn">
            🔄 New Assessment
        </button>

        <button id="dashboardBtn">
            🏠 Dashboard
        </button>

    </div>

</div>

`;

document.getElementById("newAssessmentBtn").onclick = () => {
    location.reload();
};

document.getElementById("dashboardBtn").onclick = () => {
    window.location.href = "/dashboard";
};

        } else {

            showToast(result.message);

        }

    } catch (error) {


        loadingContainer.style.display = "none";

        questionContainer.style.display = "block";
        document.querySelector(".navigation-buttons").style.display = "flex";
        submitBtn.disabled = false;
        submitBtn.innerText = "Submit Assessment";



        showToast("Server Error! Please try again.");

        console.error(error);

    }

});

// ======================================
// INITIALIZE
// ======================================

showQuestion();



// ======================================
// SHOW TOAST
// ======================================

function showToast(message) {

    toast.innerText = message;

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 3000);

}