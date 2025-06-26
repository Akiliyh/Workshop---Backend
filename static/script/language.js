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
            let gender = document.querySelector('.gender');

            document.title = data.nameLanguage;
            speakers.textContent = data.totalSpeakers;
            name.textContent = data.nameLanguage;
            gender.textContent = (data.gender === 0) ? 'Non-gendered' : 'Gendered';


            fetch('/api/word_order/' + data.idWordOrder, {
                method: 'GET',
            })
                .then(res => res.json())
                .then(dataWO => {
                    wordOrder.textContent = dataWO.name;
                })
        })

    fetch('/api/country/language/' + poiId, {
        method: 'GET',
    })
        .then(res => res.json())
        .then(dataC => {
            let countries = document.querySelector('.countries');

            dataC.forEach(dataC => {
                const link = document.createElement('a');
                link.href = '/country/' + dataC.idCountry;
                link.textContent = dataC.nameCountry;
                countries.appendChild(link);
            });
        })
});