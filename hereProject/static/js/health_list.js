//input 태그에서 검색한 카테고리만 보임
const searchInput = document.getElementById('name'); // input 태그 검색 text

const searchButton = document.querySelector('.search img');
const workoutCategories = document.querySelectorAll('.workout-category');

searchButton.addEventListener('click', () => {
  const searchTerm = searchInput.value.trim(); // 문자열 앞뒤 공백 제거

  let matchFound = false;
  workoutCategories.forEach((category) => {
    const categoryName = category.querySelector('h2').textContent;
    if (categoryName === searchTerm) {
      category.style.display = 'block';
      matchFound = true;
    }
     else {
      category.style.display = 'none';
    }
  });

  if (!matchFound) {
    workoutCategories.forEach((category) => {
      category.style.display = 'none';
    });
  }
});