function foo() {

    fetch('http://localhost:5000/messages')
        .then((response) => {
            return response.json();
        })
        .then((myJson) => {
            rewriteMessages(myJson);
        });
    setTimeout(foo, 5000);
}

function rewriteMessages(myJson) {
    document.getElementById("tbody").innerHTML = '';
    // console.log('pop ', myJson);
    for (let i=0; i < myJson.length; i++) {
        let messageRow = document.createElement('tr');
        messageRow.innerHTML = `
            <td>${myJson[i].username}: ${myJson[i].message}</td>
        `;
        document.getElementById("tbody").appendChild(messageRow);
    }
}

foo();
