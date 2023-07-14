var checkboxes = document.querySelectorAll('.check');
var clearButton = document.querySelector('.clearbtn');
var popWrap = document.querySelector('#pop_info_1');
var btnClose = document.querySelector('.btn_close');
var innerText = document.querySelector('.dsc'); //팝업창 내의 텍스트

//5번 체크 시 운동왕, 10번 체크 시 성실왕, 15번 체크 시 끈기왕
function checkCheckboxCount() {
  var checkedCount = document.querySelectorAll('.check:checked').length;
  if (checkedCount === 5) {
    popWrap.style.display = 'block';
    innerText.innerHTML="💪운동왕 달성카드 획득! mypage에서 확인하세요💖";
  }
  if(checkedCount === 10)
  {
    popWrap.style.display = 'block';
    innerText.innerHTML="💪성실왕 달성카드 획득! mypage에서 확인하세요💖";
  }
  if(checkedCount === 15)
  {
    popWrap.style.display = 'block';
    innerText.innerHTML="💪끈기왕 달성카드 획득! mypage에서 확인하세요💖";
  }
}

btnClose.addEventListener('click', function () {
  popWrap.style.display = 'none';
});


checkboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    checkCheckboxCount();
  });
});
