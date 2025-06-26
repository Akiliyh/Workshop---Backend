document.addEventListener("DOMContentLoaded", () => {

    const poiId = poiData.id;

    document.getElementById("delete-btn").addEventListener("click", async () => {
        fetch('/api/language/' + poiId, {
            method: 'DELETE',
        }).then(res => res.text())
            .then(res => {
                console.log("Delete success:", res);
                window.location.href = "/";
            })
    });

    fetch('/api/language/' + poiId, {
        method: 'GET',
    })
        .then(res => res.json())
        .then(data => {
            let wordOrder = document.querySelector('.word-order');
            let speakers = document.querySelector('.speakers');
            let name = document.querySelector('.name');

            document.title = data.nameLanguage;
            speakers.textContent = data.totalSpeakers;
            name.textContent = data.nameLanguage;


            fetch('/api/word_order/' + data.idWordOrder, {
                method: 'GET',
            })
                .then(res => res.json())
                .then(dataWO => {
                    wordOrder.textContent = dataWO.name;

                })
        })
});