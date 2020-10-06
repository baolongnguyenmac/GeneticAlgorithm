# Solving Quadratic Equation using Genetic Algorithm  

Áp dụng thuật giải Genetic để giải phương trình bậc 2  

## Ý tưởng  

- Generate ngẫu nhiên 1 quần thể với số lượng cá thể `200`  
- Đánh giá các cá thể trong quần thể theo fitnessFuncion: ![](https://latex.codecogs.com/svg.latex?\inline&space;|ax^{2}&plus;bx&plus;c|)  
    * Giá trị thu được càng gần `0` thì càng tốt  
    * Giá trị thu được sẽ được lưu trữ tăng dần trong 1 mảng, ứng với mỗi giá trị `x` được chọn ngẫu nhiên  
- Loại bỏ một nửa số lượng các cá thể có fitness thấp  
- Các cá thể còn trụ lại được đem đi lai ngẫu nhiên với nhau và thu được 1 quần thể có số lượng như ban đầu  
- Lặp lại quá trình trên cho đến khi thu được 1 giá trị ![](https://latex.codecogs.com/svg.latex?\inline&space;\varepsilon) sao cho ![](https://latex.codecogs.com/svg.latex?\inline&space;|ax_{0}^{2}&plus;bx_{0}&plus;c|\leq&space;\varepsilon)  
    * ![](https://latex.codecogs.com/svg.latex?\inline&space;\varepsilon) có thể tuỳ chọn. Trong bài là `0.0001`  

## Thực hiện  

- Thực hiện lai  
    * Sau khi lựa chọn được 2 đối tượng để lai, ta biểu diễn 2 đối tượng này dưới dạng nhị phân `32 hoặc 64 bit`  
    * Chọn random 1 số nguyên trong khoảng từ 0 đến `32 - 1 hoặc 64 - 1`  
    * Cắt 2 dãy bit bên trên tại vị trí ứng với số nguyên vừa random sau đó đổi chéo qua cho nhau  
    * Lặp lại quá trình lai cho đến khi số cá thể trong quần thể bằng với số cá thể trong quần thể ban đầu  
- Thực hiện chọn khoảng nghiệm  
    * Tính giá trị đỉnh của parabol: ![](https://latex.codecogs.com/svg.latex?\inline&space;-\frac{b}{2a})  
    * Random 1 số thực dương, trong bài này là 1 số thực ![](https://latex.codecogs.com/svg.latex?\inline&space;b_{0}): ![](https://latex.codecogs.com/svg.latex?\inline&space;0\leq&space;b_{0}\leq&space;10)  
    * Nghiệm sẽ được chọn random trong khoảng: ![](https://latex.codecogs.com/svg.latex?\inline&space;x_{0}-b_{0}\leq&space;x\leq&space;x_{0}&plus;b_{0})  
- Thực hiện chọn lọc trong quần thể  
    * Giống như đã mô tả trong phần ý tưởng  

## Hên xui?  

- Bài toán có khả năng rơi vào trường hợp generate một quần thể với các giá trị `x` giống hệt nhau. Giá trị `x` này xấp xỉ bằng nghiệm cần tìm nhưng lại không thoả mãn điều kiện của ![](https://latex.codecogs.com/svg.latex?\inline&space;\varepsilon)  
- Trong trường hợp này, xuất hiện 1 vòng lặp vô tận trong hàm `mate()` hoặc hàm `run()`  
