document.addEventListener('DOMContentLoaded', () =>{
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const resultBox = document.getElementById('results-box');

    const searchWorkouts = (workout) => {
        $.ajax({
            method: 'POST',
            url: searchUrl,
            data: {
                'csrfmiddlewaretoken': csrf_token,
                'workout': workout,
            },
            success: (response) => {
                console.log(response.data);
                const data = response.data;
                if (Array.isArray(data)){
                    resultBox.innerHTML = "";
                    data.forEach(workout =>{
                        resultBox.innerHTML += `
                        <a href="/fitnessTracker/workout/${workout.slug}/" class="workout">
                            <div class="row">
                                <div class="col">
                                    <h3>${workout.name}</h3>
                                    <p>Duration: ${workout.duration}</p>
                                </div>
                            </div>
                        </a>
                        `;
                    })
                } else {
                    if (searchInput.value.length > 0){
                        resultBox.innerHTML = `<b>${data}</b>`;
                    } else {
                        resultBox.classList.add('not-visible');
                    }
                }
            },
        });
    };

    searchInput.addEventListener('keyup', e=>{
        console.log(e.target.value)

        if (resultBox.classList.contains('not-visible')){
            resultBox.classList.remove('not-visible');
        }

        searchWorkouts(e.target.value);
    });
});