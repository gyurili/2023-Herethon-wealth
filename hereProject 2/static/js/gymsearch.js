const Btn1 = document.querySelector('.w1'); // 전체
const Btn2 = document.querySelector('.w2');
const Btn3 = document.querySelector('.w3');
const Btn4 = document.querySelector('.w4');
const armCategories = document.querySelectorAll('.gym-container > div');

Btn1.addEventListener('click', () => {
  armCategories.forEach((category) => {
    category.style.display = 'block';
  });
});

Btn2.addEventListener('click', () => {
  armCategories.forEach((category) => {
    if (!category.classList.contains('fifth_2')) {
      category.style.display = 'none';
    } else {
      category.style.display = 'block';
    }
  });
});

Btn3.addEventListener('click', () => {
  armCategories.forEach((category) => {
    if (category.classList.contains('fifth_2') || category.classList.contains('fifth_3')) {
      category.style.display = 'block';
    } else {
      category.style.display = 'none';
    }
  });
});

Btn4.addEventListener('click', () => {
  armCategories.forEach((category) => {
    if (category.classList.contains('fifth_1')) {
      category.style.display = 'block';
    } else {
      category.style.display = 'none';
    }
  });
});