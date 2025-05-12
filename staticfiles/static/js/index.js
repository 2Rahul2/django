import { GetData } from "/static/js/sentiment.js";

// const { GetData } = require("./sentiment");

document.getElementById("sentimentForm").addEventListener("submit",async function(event) {
    event.preventDefault();
    const productName = document.getElementById("productName").value.trim();

    if (true) {
        const loadingElement = document.getElementById("loading");

        // Show loading animation
        loadingElement.style.display = "block";
        // let data = null;
        let data =await GetData(productName.toLowerCase())
        console.log(data)
        if (data) {
            loadingElement.style.display = "none";
            console.log(data);  // Check the response in the console
            
            // Update the title
            document.getElementById("productTitle").textContent = productName;
            
            // Update the summary
            document.getElementById("productSummary").textContent = data.summary;

            // Populate pros and cons table
            populateProsConsTable(data.pros.items, data.cons.items);

            // Populate recommendations
            populateRecommendations(data.recommendations);

            // Show result section
            document.getElementById("result").style.display = "block";
            // Assuming the response contains a structure like this (from GetSummary)
            const prosPercentage = data.pros.percentage;  // Get the percentage of pros from the response
            const consPercentage = data.cons.percentage;  // Get the percentage of cons from the response

            // Ensure the total percentage adds up to 100
            const otherPercentage = 100 - (prosPercentage + consPercentage);

            // Prepare the data for the chart
            const ctx = document.getElementById("prosConsChart").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: ["Pros", "Cons", "Other"],  // Added 'Other' for cases where pros + cons < 100%
                    datasets: [{
                        data: [prosPercentage, consPercentage, otherPercentage],  // Use dynamic percentages here
                        backgroundColor: ["#28a745", "#dc3545", "#ffc107"],  // Green for pros, red for cons, yellow for other
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    const total = tooltipItem.dataset.data.reduce((sum, value) => sum + value, 0);
                                    const percentage = Math.round((tooltipItem.raw / total) * 100);
                                    return tooltipItem.label + ": " + percentage + "%";
                                }
                            }
                        }
                    }
                }
            });
            loadingElement.style.display = "none";

        } else {
            alert("No sentiment analysis data found.");
        }
        document.getElementById("productTitle").textContent = productName;
        // document.getElementById("result").style.display = "block";

    } else {
        document.getElementById("result").style.display = "none";
        alert("Sentiment analysis is only available for Samsung S24.");
    }
});


function populateProsConsTable(pros, cons) {
    let tableHTML = `
        <tr>
            <th>Pros</th>
            <th>Cons</th>
        </tr>
    `;

    const maxRows = Math.max(pros.length, cons.length);

    for (let i = 0; i < maxRows; i++) {
        const proText = pros[i] || ""; // If no pro available, leave empty
        const conText = cons[i] || ""; // If no con available, leave empty
        tableHTML += `
            <tr>
                <td>${proText}</td>
                <td>${conText}</td>
            </tr>
        `;
    }

    document.querySelector("table").innerHTML = tableHTML;
}

/**
 * Function to populate recommended products
 */
function populateRecommendations(recommendations) {
    let recommendationsHTML = recommendations.map(rec => `
        <li><strong>${rec.product_name}</strong> - ${rec.why_recommended}</li>
    `).join("");

    document.querySelector(".recommendations ul").innerHTML = recommendationsHTML;
}