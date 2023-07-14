const bodyweightBtn1 = document.querySelector('.w1'); //전체
const bodyweightBtn2 = document.querySelector('.w2'); //맨몸
const armCategories = document.querySelectorAll('.arm-container > div');
bodyweightBtn1.addEventListener('click',()=>{
    armCategories.forEach((category, index) => {
          category.style.display = 'block';
})
})

bodyweightBtn2.addEventListener('click', () => {
  armCategories.forEach((category, index) => {
    if (index >= 4 && index <= 6) {
      category.style.display = 'none';
    } else {
      category.style.display = 'block';
    }
  });
});
