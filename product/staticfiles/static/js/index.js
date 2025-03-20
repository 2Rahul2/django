import { GetData } from "./sentiment";

document.getElementById("sentimentForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const productName = document.getElementById("productName").value.trim();

    if (productName.toLowerCase() === "samsung s24") {
        let data = GetData()
        document.getElementById("productTitle").textContent = productName;
        document.getElementById("result").style.display = "block";

        const ctx = document.getElementById("ratingChart").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["1 Star", "2 Stars", "3 Stars", "4 Stars", "5 Stars"],
                datasets: [{
                    label: "Number of Users",
                    data: [10, 25, 40, 100, 250],  // Dummy data
                    backgroundColor: ["#ff4c4c", "#ffae42", "#ffd700", "#90ee90", "#008000"]
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        document.getElementById("result").style.display = "none";
        alert("Sentiment analysis is only available for Samsung S24.");
    }
});