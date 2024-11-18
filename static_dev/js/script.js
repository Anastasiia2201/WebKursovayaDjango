function showCourse(course) {
    const semesters = document.querySelectorAll('.semester-block');
    semesters.forEach(semester => {
        semester.style.display = 'none'; // Скрыть все семестры
    });
    // Показать семестры для выбранного курса
    for (let i = 1; i <= 2; i++) { // Каждый курс имеет 2 семестра
        const semesterToShow = document.getElementById(`semester${(course - 1) * 2 + i}`);
        if (semesterToShow) {
            semesterToShow.style.display = 'block'; // Показать семестр
        }
    }
}

function toggleSubjects(subjectsId) {
    const subjects = document.getElementById(subjectsId);
    subjects.style.display = subjects.style.display === 'none' ? 'block' : 'none'; // Переключить видимость
}

// Добавление отладочной информации
console.log("Script loaded"); // Проверка, что скрипт загружен



document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('.toggle-files');
    const fileList = document.querySelector('.file-list');

    toggleButton.addEventListener('click', () => {
        fileList.classList.toggle('hidden');
        toggleButton.textContent = fileList.classList.contains('hidden') ? 'Показать файлы' : 'Скрыть файлы';
    });
});
