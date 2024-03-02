// getting the add section
const add_task = document.querySelector('.add-task');
const btnCreateTask = document.querySelector('.btn-create-task');
const btnAddTask = document.querySelector('.btn-add');
const textArea = document.getElementsByTagName("textarea")[0];

console.log("ok");

// getting the container task section
const container_task = document.querySelector('.container-tasks');

// getting the task filter container
// const task_filter = document.querySelector('.task-filter');
// getting the task filter btns
// const btnFilters = document.querySelectorAll('.btn-filter');

// add task button function - remove task container and show add task form
btnCreateTask.addEventListener('click', function () {
    console.log(textArea);
    add_task.style.display = 'flex';
    btnCreateTask.style.display = 'none';
    container_task.style.display = 'none';
});

// active class
task_filter.addEventListener('click', function (e){
    btnFilters.forEach(function (btn) {
        btn.style.opacity = .3;
        e.target.style.opacity = 1;
    });
});


// for (let i = 0; i < btnFilters.length; i++) {
//     btnFilters[i].addEventListener('click', function () {
//         this.style.opacity = 1;
//         if (i < btnFilters.length - 1){
//             btnFilters[i+1]
//         }
//     });
    
// }


