// ==========================================
// Form Submit
// ==========================================

const form = document.getElementById("assessmentForm");

const loading = document.getElementById("loading");

const result = document.getElementById("result");

form.addEventListener("submit", async function(event){

    event.preventDefault();

    loading.style.display = "block";

    result.style.display = "none";



    const data = {

        age: Number(document.getElementById("age").value),

        gender: document.getElementById("gender").value,

        employment_status:
            document.getElementById("employment_status").value,

        relationship_status:
            document.getElementById("relationship_status").value,

        sleep_hours:
            Number(document.getElementById("sleep_hours").value),

        sleep_quality:
            Number(document.getElementById("sleep_quality").value),

        food_quality:
            Number(document.getElementById("food_quality").value),

        water_intake:
            Number(document.getElementById("water_intake").value),

        exercise_hours:
            Number(document.getElementById("exercise_hours").value),

        screen_time:
            Number(document.getElementById("screen_time").value),

        hobbies_time:
            Number(document.getElementById("hobbies_time").value),
                    work_stress:
            Number(document.getElementById("work_stress").value),

        academic_pressure:
            Number(document.getElementById("academic_pressure").value),

        financial_stress:
            Number(document.getElementById("financial_stress").value),

        social_interaction:
            Number(document.getElementById("social_interaction").value),

        family_support:
            Number(document.getElementById("family_support").value),

        daily_productivity:
            Number(document.getElementById("daily_productivity").value),

        health_issues:
            Number(document.getElementById("health_issues").value)

    };



    try{

        const response = await fetch("/predict",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(data)

        });

        const output = await response.json();
                loading.style.display = "none";

        if(output.status !== "success"){

            alert(output.message || "Prediction failed.");

            return;

        }

        result.style.display = "block";

        document.getElementById("mental_state").textContent =
            output.mental_state;

        document.getElementById("mental_score").textContent =
            output.mental_score;

        document.getElementById("anxiety_score").textContent =
            output.anxiety_score;

        document.getElementById("depression_score").textContent =
            output.depression_score;

        document.getElementById("risk_level").textContent =
            output.risk_level;

        document.getElementById("recommendation").textContent =
            output.recommendation;

        result.scrollIntoView({

            behavior:"smooth"

        });

    }

    catch(error){

        loading.style.display = "none";

        alert("Unable to connect to the server.");

        console.error(error);

    }

});