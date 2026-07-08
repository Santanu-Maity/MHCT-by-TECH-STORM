async function loadHistory(){

    const response = await fetch("/history");

    const data = await response.json();

    const container = document.getElementById("historyContainer");

    container.innerHTML = "";

    data.history.forEach(item=>{

        container.innerHTML += `
            <div class="card">

                <h2>${item.mental_state}</h2>

                <p><b>Risk Level:</b> ${item.risk_level}</p>

                <p><b>Mental Score:</b> ${item.mental_score}</p>

                <p><b>Anxiety Score:</b> ${item.anxiety_score}</p>

                <p><b>Depression Score:</b> ${item.depression_score}</p>

                <p><b>Recommendation:</b> ${item.recommendation}</p>

                <p><b>Date:</b> ${item.created_at}</p>

            </div>
        `;

    });

}

loadHistory();