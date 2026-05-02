## Question
![](/assets/q_idempotency.png)
## Response Section

### ความหมาย
การเรียก API เดิม ซ้ำหลายๆ ครั้งจะได้ผลเดิมเหมือนเรียกครั้งเดียว

มีประโยชน์ ในกรณีที่ client เรียก API ซ้ำหลายครั้ง อาจจะเกิดจากความไม่แน่ใจ หรือความผิดพลาดของระบบ การมี Idempotncy จะช่วยป้องกันไม่ให้เกิดข้อผิดพลาดขึ้น

- เป็น Idempotency (GET, PUT, DELETE)
- ไม่เป็น Idempotency (POST, PATCH)

### EX. ทำให้ POST เป็น Idempotency


