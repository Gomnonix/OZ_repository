const data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
];

const dataTable = document.getElementById('data-table');

    // 데이터 표시 함수
    function displayData(dataList) {
      dataTable.innerHTML = ''; 

      dataList.forEach((item, index) => {
        const row = dataTable.insertRow(); 

        const checkboxCell = row.insertCell(0);
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `checkbox${index}`;
        checkboxCell.appendChild(checkbox); 
        // 카테고리 추가
    
        row.insertCell(1).innerHTML = item.category;
        row.insertCell(2).innerHTML = item.brand;
        row.insertCell(3).innerHTML = item.product;
        row.insertCell(4).innerHTML = item.price;
       
    })
};

displayData(data);



          
//조회 버튼 이벤트
const searchButton = document.querySelector('.btn-ser');
searchButton.addEventListener('click', function() {
    const keyword = document.getElementById('product').value.toLowerCase(); 
    const filteredData = data.filter(item => 
        item.category.toLowerCase().includes(keyword) || 
        item.brand.toLowerCase().includes(keyword) || 
        item.product.toLowerCase().includes(keyword)
    );
    displayData(filteredData);
});

// 카테고리 이벤트
document.getElementById('inlineFormSelectPref').addEventListener('change', function() {
    const selectedCategory = this.value;
    if (selectedCategory === '카테고리') {
        displayData(data);
    } else {
        const filteredData = data.filter(item => item.category === selectedCategory);
        displayData(filteredData);
    }
});



// 삭제버튼 이벤트 리스너 추가
const deleteButton = document.querySelector('.btn-del');
deleteButton.addEventListener('click', function() {
    // 체크된 체크박스 모두 가져오기
    const checkedCheckboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    

    checkedCheckboxes.forEach(checkbox => {
        const row = checkbox.parentNode.parentNode;
        row.remove();
    });
});


//현재 날짜 구현
    document.addEventListener("DOMContentLoaded", function() {
        const today = new Date();
        const year = today.getFullYear();
        const month = today.getMonth() + 1;
        const date = today.getDate();
        const dateString = `${year}-0${month}-${date}`;
    
        const heading = document.querySelector('h3');
        heading.textContent += `(${dateString})`;
    });