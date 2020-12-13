document.addEventListener('DOMContentLoaded', function () {

    var deletetodo = document.querySelectorAll('#deletetodo');
    deletetodo.forEach((item)=>{
        item.addEventListener('click', ()=>{
            var id = item.dataset.id;
            console.log(`#todoitem${id}`);
            var todoitem = document.querySelector(`#todoitem${id}`);
            todoitem.style.display = 'none';
            fetch(`/delete/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    type: "deletetodo",
                })
            })
            .then();
        });
    });

    var deletelist = document.querySelectorAll('#deletelist');
    deletelist.forEach((item)=>{
        item.addEventListener('click', ()=>{
            var id = item.dataset.id;
            var name = item.dataset.name;
            if(confirm(`"${name}" will be deleted. Are you sure?`)){
                var listitem = document.querySelector(`#list${id}`);
                listitem.style.display = 'none';
                fetch(`/delete/${id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        type: "deletelist",
                    })
                })
                .then();
            }
        });
    });

    var checkeditems = document.querySelectorAll('.form-check-input');
    checkeditems.forEach((item)=>{
        item.addEventListener('change', ()=>{
            var id = item.dataset.id; 
            var name = item.dataset.name;
            var span = document.querySelector(`#span${id}`);
            var typevalue = "";
            if(item.checked){
                typevalue = "True";
                span.innerHTML= `<del class="font-italic">${name}</del>`;
            } else {
                typevalue = "False";
                span.innerHTML= `${name}`;
            }
            fetch(`/updatestatus`, {
                method: 'PUT',
                body: JSON.stringify({
                    type: "status",
                    typevalue: typevalue,
                    todoid: id,
                })
            })
            .then();
        });
    });

});
