// getting the add section
const add_task = document.querySelector('.add-task');
const btnCreateTask = document.querySelector('.btn-create-task');
const btnAddTask = document.querySelector('.btn-add');
const textArea = document.getElementsByTagName("textarea")[0];
const btnCancel = document.querySelector('.btn-cancel');
const upcoming = document.querySelector('.upcoming');
const overdue = document.querySelector('.overdue');
const all_task = document.querySelector('.all_tasks');
const btn_upcoming = document.querySelector('.btn-upcoming');
const btn_overdue = document.querySelector('.btn-overdue');
const btn_all = document.querySelector('.btn-all');

// getting the container task section
const container_task = document.querySelector('.container-tasks');

// getting the task filter container
const task_filter = document.querySelector('.task-filter');

const btnFilters = document.querySelectorAll('.btn-filter');

// add task button function - remove task container and show add task form
btnCreateTask.addEventListener('click', function () {
    // console.log(textArea);
    add_task.style.display = 'flex';
    btnCreateTask.style.display = 'none';
    container_task.style.display = 'none';
});

btnCancel.addEventListener('click', function (){
    add_task.style.display = 'none';
    btnCreateTask.style.display = 'block';
    container_task.style.display = 'flex';
} )

// active class
// task_filter.addEventListener('click', function (e){
//     btnFilters.forEach(function (btn) {
//         e.target.style.opacity = 1;
//         btn.style.opacity = .3;
//     });
// });

btn_upcoming.addEventListener('click', function(){
    upcoming.style.display = 'table-row-group';
    overdue.style.display = 'none';
    all_task.style.display = 'none';

    btn_upcoming.style.opacity = 1;
    btn_overdue.style.opacity = .3;
    btn_all.style.opacity = .3;
});

btn_overdue.addEventListener('click', function(){
    upcoming.style.display = 'none';
    overdue.style.display = 'table-row-group';
    all_task.style.display = 'none';

    btn_upcoming.style.opacity = .3;
    btn_overdue.style.opacity = 1;
    btn_all.style.opacity = .3;
});

btn_all.addEventListener('click', function(){
    upcoming.style.display = 'none';
    overdue.style.display = 'none';
    all_task.style.display = 'table-row-group';

    btn_upcoming.style.opacity = .3;
    btn_overdue.style.opacity = .3;
    btn_all.style.opacity = 1;
});


// for (let i = 0; i < btnFilters.length; i++) {
//     btnFilters[i].addEventListener('click', function () {
//         this.style.opacity = 1;
//         if (i < btnFilters.length - 1){
//             btnFilters[i+1]
//         }
//     });
    
// }


