document.addEventListener("DOMContentLoaded", () => {
    const poiId = poiData.id;

    document.getElementById("delete-btn").addEventListener("click", async () => {
        fetch('/api/country/' + poiId, {
            method: 'DELETE',
        }).then(res => res.text())
            .then(res => {
                console.log("Delete success:", res);
                window.location.href = "/";
            })
    });

    fetch('/api/country/' + poiId, {
        method: 'GET',
    })
    .then(res => res.json())
    .then(data => {      
        let desc = document.querySelector('.desc');
        let inh = document.querySelector('.inhabitants');
        let gov = document.querySelector('.gov');
        let date = document.querySelector('.date');
        let capital = document.querySelector('.capital');
        let name = document.querySelector('.name');
        
        desc.textContent = data.descCountry;
        inh.textContent = data.inhabitants + ' inhabitants';
        gov.textContent = data.governmentType;
        date.textContent = data.date;
        capital.textContent = data.capital;
        name.textContent = data.nameCountry;
        document.title = data.nameCountry;

    })


});