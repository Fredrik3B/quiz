function validateResponse(response) {
      if (!response.ok) {
              throw Error(response.statusText);
            }
      return response.json();
}

fetch("api/").then(validateResponse).then(data => console.log(data)
)


