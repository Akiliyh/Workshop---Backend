document.addEventListener("DOMContentLoaded", () => {

    const poiId = poiData.id;

    document.getElementById("delete-btn").addEventListener("click", async () => {
        fetch('/api/point_of_interest/' + poiId, {
            method: 'DELETE',
        }).then(res => res.text())
            .then(res => {
                console.log("Delete success:", res);
                window.location.href = "/";
            })
    });

    // document.getElementById("modify-btn").addEventListener("click", async () => {
    //     const poiId = poiData.id;
    //     fetch('/api/point_of_interest/' + poiId, {
    //         method: 'PUT',
    //     }).then(res => res.text())
    //         .then(res => {
    //             console.log("Modify success:", res);
    //             // window.location.href = "/point_of_interest/" + poiId;
    //         })
    // });

    fetch('/api/point_of_interest/' + poiId, {
        method: 'GET',
    })
        .then(res => res.json())
        .then(data => {
            let desc = document.querySelector('.desc');
            let date = document.querySelector('.date');
            let country = document.querySelector('.country');
            let type = document.querySelector('.type');
            let name = document.querySelector('.name');

            desc.textContent = data.descInterestPoint;
            date.textContent = data.dateInterestPoint;
            name.textContent = data.nameInterestPoint;
            document.title = data.nameInterestPoint;

            fetch('/api/country/' + data.idCountry, {
                method: 'GET',
            })
                .then(res => res.json())
                .then(dataCountry => {

                    const link = document.createElement('a');
                    link.href = '/country/' + data.idCountry;
                    link.textContent = dataCountry.nameCountry;

                    country.textContent = '';
                    country.appendChild(link);

                })

            fetch('/api/type_of_point/' + data.idType, {
                method: 'GET',
            })
                .then(res => res.json())
                .then(dataType => {

                    const iconMap = {
                        'body of water': 'fa-water',
                        'statue': 'fa-person',
                        'monument': 'fa-landmark',
                        'castle': 'fa-chess-rook',
                        'beach': 'fa-umbrella-beach',
                        'park': 'fa-leaf',
                        'forest': 'fa-tree',
                    };

                    const icon = document.createElement('i');
                    const name = document.createElement('p');
                    const iconClass = iconMap[dataType.name.toLowerCase()];

                    icon.classList.add('fa-solid', iconClass);
                    icon.style.color = 'white';
                    name.textContent = dataType.name;

                    type.appendChild(icon);
                    type.appendChild(name);

                })
        })
});