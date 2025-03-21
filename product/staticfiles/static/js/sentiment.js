// document.addEventListener("DOMContentLoaded", function() {
//     document.getElementById("sentimentForm").addEventListener("submit", function(event) {
//         event.preventDefault();
        
//         let productName = document.getElementById("productName").value;
//         let resultDiv = document.getElementById("result");
        
//         // Simulating an API call (Replace with actual AJAX request in Django)
//         resultDiv.innerHTML = `<p class="text-blue-600">Analyzing sentiment for <b>${productName}</b>...</p>`;
//         resultDiv.classList.remove("hidden");
//         axios.get('sentiment/' ,{
//             params:{product:productName}
//         }).then(response => {
//             console.log(response.data)
//             console.log(response.data.summary)
//             let sentiment = response.data.data;
//             resultDiv.innerHTML = `<p class="text-gray-700">Sentiment: <span class="font-bold">${sentiment}</span></p>`;
//         })
//         .catch(error => {
//             resultDiv.innerHTML = `<p class="text-red-600">Error fetching sentiment data.</p>`;
//             console.error("Error:", error);
//         });
//     });
// });

export const GetData = async (productName) => {
    try {
        const response = await axios.get('sentiment/', {
            params: { product: productName }
        });
        console.log(response.data); // ✅ This logs the correct JSON
        return response.data; // ✅ This correctly returns the data
    } catch (error) {
        console.error("Error fetching data:", error);
        return null; // Ensure null is returned in case of failure
    }
};

