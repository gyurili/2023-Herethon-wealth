const categoryItems = document.querySelectorAll('.arm-container > div');
const addButton = document.querySelector('.plusbtn');
const successMessage = document.querySelector('.plusmsg');

categoryItems.forEach((item) => {
  item.addEventListener('click', (event) => {
    event.preventDefault();
    item.classList.toggle('selected');
  });
});

addButton.addEventListener('click', () => {
  categoryItems.forEach((item) => {
    item.classList.remove('selected');
  });
  successMessage.style.display = 'block';
  setTimeout(() => {
    successMessage.style.display = 'none';
  }, 1000);
});
