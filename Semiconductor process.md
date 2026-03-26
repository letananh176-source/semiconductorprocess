# **[[1. Kéo tinh thể Silicon]]**

Nồi thạch anh + Silicon đa tinh thể
Temperature > $1400^o$ C vì nhiệt độ nóng chảy của Si là 1414°C trong phương pháp Czochralski
Thả tinh thể mầm + kéo

**Thu được thanh Silicon đơn tinh thể, dài**. Sau đó mài nhẵn
![[Pasted image 20260326163557.png]]

# **[[2. Cắt lát Silicon]]**

Dây thép + bột kim cương siêu nhỏ
==> Tấm Silicon
Sau khi cắt: mài nhẵn, đánh bóng, bo góc để đạt độ hoàn chỉnh cần thiết
# **[[3. Oxidation - oxi hoá]]**

![[Pasted image 20260326164520.png]]
Silicon đơn tinh thể rất nhạy cảm, dễ nhiễm bẩn. Để bảo vệ, phủ lên một lớp $SiO_2$
Tại sao lại chọn $SiO_2$ : cách điện, ngăn dòng rò, chắn tạp chất
![[Pasted image 20260326164649.png]]
**Oxi hoá**
1: Ngoài không khí có phản ứng với $O_2$ => $SiO_2$
![[Pasted image 20260326164759.png]]

2: Lò, tốc độ nhanh hơn.
![[Pasted image 20260326164812.png]]
Sau bước này, tấm wafer có lớp phủ $SiO_2$ bảo vệ
# **[[4. Photoresist Coating - Phủ quang trở]]**

Đặt Wafer lên **bàn hút chân không có thể xoay**, quay phủ.
![[Pasted image 20260326164935.png]]
Vancuum chunk
Quay + nhỏ dung dịch quang trở
Do lực li tâm => lớp mỏng và đồng đều
![[Pasted image 20260326165012.png]]
**Tại sao lại là chân không?**
Chân không: rãnh đồng tâm siêu nhỏ hoặc gốm xốp chằn chịt lỗ li ti, độ cứng cơ học của Wafer => không làm cong Wafer
**! rủi ro duy nhất**: bụi, gây out of focus trong phước photolithography.
Các cách khác: dễ làm hỏng wafer, không sạch quy trình.
# **[[5. Photolithography - quang khắc]]**

Ánh sáng truyền mô hình từ mặt nạ sang lớp PR
![[Pasted image 20260326165357.png]]
![[Pasted image 20260326165405.png]]
Ánh sáng được dùng là tia cực tím (UV) đến siêu cực tím (EUV)
Các bước sóng tiêu chuẩn trong ngành (không dùng ánh sáng khả kiến vè bước sóng quá dài (năng lượng thấp)):
**Đèn hơi thuỷ ngân -Mercury Arc Lamp**: công nghệ cũ, các lớp linh kiện to
G-line: 436nm
I-line: 365nm
**Laser excimer - Deep UV - DUV**: dùng hầu hết cho các chip tiêu chuẩn hiện nay.
KrF (Krypton Flouride): 248nm
ArF (Argon Flouride): 193nm (kết hợp với Immersion lithography - quang khắc nhún nước đề làm chip đến 7 nm)
**Extreme UV - EUV**: 13.5nm. Công nghệ mới nhát hiện nay của ASML cho các tiến trình 2, 3, 5 nm.

Phải chọn bộ quang trở và bước sóng ánh sáng phù hợp vì: photoresist đóng vai trò như công tắt quang học, chỉ hoạt đông khi hấp thụ đúng mức năng lượng photon cụ thể.

Năng lượng của ánh sáng được tính bằng hệ thức Planck - Einstein
$\displaystyle E = \frac{hc}{\lambda}$
trong đó:
h: là hằng số planck: $6,626\times10^{-34}$ 
c: tốc độ ánh sáng trong chân không $\approx 3\times 10^8$ m/s
$\lambda$: bước sóng ánh sáng ($\micro m$ hoặc nm)

Khi tiếp xúc với ánh sáng, quang trở sẽ thay đổi tính chất hoá học. 
Có 2 loại quang trở:
![[Pasted image 20260326171808.png]]
**Quang trở dương**: Phần quang trở tiếp xúc với ánh sáng sẽ bị phân huỷ quang học (photochemical degradation) và hoà tan hoàn toàn trong dung dịch hiện hình (developer) ở bước rửa tiếp theo, vùng không bị chiếu vẫn giữ nguyên, là loại PR phổ biến nhất hiện nay
**Quang trở âm**: phần PR tiếp xúc với ánh sáng sẽ cứng lại, vùng không có ánh sáng sẽ bị rửa trôi, loại này ít được dùng hơn trong các công nghệ hiện đại.
# **[[6. Development - hiển thị hình ảnh]]**

Sau khi PR được tiếp xúc với ánh sáng trong bước lithography, là bước **development** (hiển thị)

![[Pasted image 20260326171954.png]]

**Development**: là quá trình rửa trôi những phần PR không cần thiết.

![[Pasted image 20260326172046.png]]

**Nhược điểm**: ở mốc nanomet, các rãnh bị quang khắc (trenches) cực kì hẹp. Developer (dung dịch rửa - thường dùng base mạnh như TMAH 2.38%) có **lực căng bề mặt lớn**. Nếu chỉ ngâm tĩnh (immersion), chất lỏng sẽ tạo ra mặt khum (meniscus) chặn ngay miệng rãnh, hoá chất không chui xuống đáy được. **Hậu quả** rửa không sạch, cặn PR vẫn đọng dưới đáy rãnh (hiện tượng Scumming). Sau này đem khắc mạch sẽ bị chập, đứt gãy. Đồng thời hoá chất ngâm một chỗ sẽ bị bão hoà nhanh, mất khả năng hoà tan PR.

**Để khắc phục** nhược điểm của immersion: phương pháp **spray development** - hiển thị dạng phun sương.

Hệ thống bơm hoá chất qua vòi phum áp lực để tạo thành các hạt sương li ti mang động năng lớn.
Động năng này đâm thủng lực căng bề mặt, ép hoá chất tươi (fresh chemical) len lỏi vào tận dáy rãnh sâu nhất.
Dòng nước súc nửa (DI water) kết hợp với lực li tâm từ bàn quay sẽ cuốn trọn bã PR vừa bị hoà tan ra ngoài.
Ũ tĩnh (Puddle) vài giây để phản ứng hoá học bẽ gãy mạch polymer diễn ra đồng đều trên toàn bộ bề mặt wafer. Đợi PR rã ra rồi xịt và quay ly tâm để dọn. Cuối cùng là sấy khô.

Cuối cùng: đem wafer đã rửa đi nung ở nhiệt độ cao 120 - 200 độ C (**Hard bake**, nhằm kích hoạt phản ứng liên kết chéo (Cross - linking)). các mạch polymer của PR đan chặt vào nhau, cô đặt lại thành lớp siêu cứng, bám cực kì chặt trên bề mặt wafer.

Vì bước **etching** vô cùng khắc nghiệt. Nếu không được **Hard bake**, lớp PR dễ bị bong tróc, nhăn nheo, cháy rụi, làm hỏng vật liệu cần bảo vệ bên dưới.
# **[[7. Etching - Khắc]]**

Để khắc lên chip những hình ảnh đã được hiển thị trên lớp quang khắc, thực hiện bước **Etching**

![[Pasted image 20260326182158.png]]

**Etching** thật ra khá giống với **development**, đều là quá trình bóc tách vật liệu **(subtractive process)** để tạo hình.

**Development** (rửa mạch - hiện hình): bản chất là bước gọt khuôn tạm thời. Dung dịch rửa (kiềm nhẹ - như TMAH) chỉ hoà tan và dọn dẹp lớp màng polymer hữu cơ (PR) đã biến đổi hoá học bởi tia UV. Bước này diễn ra khá êm dịu, mục đích duy nhất là tạc bản vẽ mạch lên lớp màn PR để làm khiên chắn, tuyệt đối chưa xâm phạm gì đến lớp vật liệu thật cấu thành nên con chip.

**Etching**: là công đoạn đục đẽo vật liệu IC thật, cực kì phức tạp. Dựa vào tấm khiên PR vừa tạo ở trên, hệt thống sẽ dội axit mạnh (Wet etching) hoặc nã ion plasma tốc độ cao (Dry etching) để phá những vùng vật liệu không được che chắn (nền silicon, màng các điện $SiO_2$, hoặc kim loại). Đây mới chính là bước ăn mòn vật lý để tạc ra các rãnh, hố và hình hài cấu trúc thật sự của linh kiện.

Vì lớp PR đã bị loại bỏ ở bước **Development** làm lộ ra bề mặt bên dưới, cách đơn giản nhất là ngâm trong dung dịch khắc - **Wet- etching**

**Wet-etching**

>Như development, vẫn dùng Spray/spin or immersion
>**Lưu ý**: với immersion, dung dịch ăn mòn không có mắt vì thế chúng ăn mòn tất cả bề mặt tiếp xúc phù hợp với nó, nghĩa là đáy wafer cũng sẽ bị ăn mòn.
>Do đó, cần phủ màn bảo vệ mặt lưng (Backside protection): trước khi wetetching phủ mặt lưng một lớp màng mỏng không phản ứng với dung dịch khắc, thường là Silicon Nitride ($Si_3N_4$).

**Bản chất quá trình**: hoá chất lỏng sẽ phản ứng và hoà tan vật liệu không được màng PR che chắn. Nhờ đó mẫu hình (parttern) từ mặt nạ PR sẽ được truyền chính xác xuống lớp vật liệu chức năng (Ví dụ: lớp $SiO_2$, nền tinh thể Silicon, hoặc màng kim loại).
![[Pasted image 20260326182930.png]]

**Nhược điểm cốt lõi - đẳng hướng (Isotropic etching)**
Dung dịch ăn mòn hoá học theo mọi hướng bới tố độ gần như bằng nhau. hậu quả là hoá chất không chỉ khoét sâu xuống mặt đáy mà con ăn lang sang hai bên vách, chui sâu vào bên dưới lớp PR. Hiện tượng này gọi là **under-cut** (lẹm chân), làm sai lệch kích thước hình học của vi mạch thành phẩm, đặt biệt không thể ứng dụng cho các linh kiện có kích thước siêu nhỏ (nanoscale).
![[Pasted image 20260326183156.png]]
![[Pasted image 20260326183144.png]]

**Ưu điểm nổi bật - Selectivity (tỉ lệ chọn lọc) cao**
Tỷ lệ chọn lọc (ký hiệu là S) là đại lượng đặc trưng cho khả năng ăn mòn đúng mục tiêu của dung dịch, được tính bằng tỷ số giữa tốc độ ăn mòn của lớp vật liệu cần khắc và tốc độ ăn mòn của vật liệu làm mặt nạ (hoặc vật liệu nền)
$$S = \frac{R_1}{R_2}$$
Với 
S: tỷ lệ chọn lọc (không thứ nguyên). S càng lớn, quá trình khắc càng hoàn hảo.
$R_1$: tốc độ ăn mòn lớp vật liệu mục tiêu ($nm/phút$ hoặc $\micro m/phút$ )
$R_2$: tốc độ ăn mòn lớp mặt nạ PR che chắn hoặc lớp nền (đơn vị như trên)

**Tóm lại**: Nhanh, rẻ, độ chọn lọc cao, dùng chip to $>3 \micro m$, máy giặt,...

![[Pasted image 20260326183848.png]]

# **[[8.  Doping - pha tạp]]**
# **[[9. Thin film deposition - Lắng đọng màng mỏng]]**
# **[[10. Metallization - kim loại hoá]]**
