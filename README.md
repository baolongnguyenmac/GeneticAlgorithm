# Apply Genetic Algorithm on solving Quadratic Equation  

Áp dụng thuật giải Genetic để giải phương trình bậc 2  

## Ý tưởng  

- Generate ngẫu nhiên 1 quần thể với số lượng cá thể `200`  
- Đánh giá các cá thể trong quần thể theo fitnessFuncion: $ax^{2} + bx + c$  
    * Giá trị thu được càng gần `0` thì càng tốt  
    * Giá trị thu được sẽ được lưu trữ tăng dần trong 1 mảng, ứng với mỗi giá trị `x` được chọn ngẫu nhiên  
- Loại bỏ một nửa số lượng các cá thể có fitness thấp  
- Các cá thể còn trụ lại được đem đi lai ngẫu nhiên với nhau và thu được 1 quần thể có số lượng như ban đầu  
- Lặp lại quá trình trên cho đến khi thu được 1 giá trị $|ax_{0}^{2} + bx_{0} + c| \leq \varepsilon$  
    * $\varepsilon$ có thể tuỳ chọn. Trong bài là `0.0001`  

## Thực hiện  

- Thực hiện lai  
    * Sau khi lựa chọn được 2 đối tượng để lai, ta biểu diễn 2 đối tượng này dưới dạng nhị phân `32 hoặc 64 bit`  
    * Chọn random 1 số nguyên trong khoảng từ 0 đến `32 - 1 hoặc 64 - 1`  
    * Cắt 2 dãy bit bên trên tại vị trí ứng với số nguyên vừa random sau đó đổi chéo qua cho nhau  
    * Lặp lại quá trình lai cho đến khi số cá thể trong quần thể bằng với số cá thể trong quần thể ban đầu  
- Thực hiện chọn khoảng nghiệm  
    * Tính giá trị đỉnh của parabol: $-\frac{b}{2a}$  
    * Random 1 số thực dương, trong bài này là 1 số thực $b_{0}$: $0\leq b_{0}\leq 10$  
    * Nghiệm sẽ được chọn random trong khoảng: $x_{0}-b_{0}\leq x\leq x_{0}+b_{0}$  
- Thực hiện chọn lọc trong quần thể  
    * Giống như đã mô tả trong phần ý tưởng  
$`\sqrt{2}`$  
