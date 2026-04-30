## Question
![](/assets/q_acid.png)
## Response Section

### ACID เป็นคอนเซปในการทำธุระกรรม Transaction ให้เป็นไปอย่างถูกต้องและปลอดภัย

### Transaction จะประกอบด้วย sql statement หลายตัวรวมกัน
เช่น โอนเงินจากบัญชี A ไป B จะเกิด 2 sql statement รวมเป็น 1 transaction
1. sql statement ถอนเงินจากบัญชี A
2. sql statement รับเงินเข้าบัญชี B

ใช้ Explicit Transaction 
- BEGIN เพื่อดูผลลัพธ์ที่ได้
- COMMIT เพื่อยืนยัน
- ROLLBACK เมื่อผลลัพธ์ไม่ถูกต้อง

### ACID 

#### Atomicity

ทุก sql statement ไม่สามารถแบ่งแยกได้ ต้องทำงานสำเร็จทั้งหมดถึงจะนับเป็น transaction ที่สมบูรณ์
หากไม่สำเร็จตัวใดตัวหนึ่งถือว่า transaction นี้ไม่สมบูรณ์และข้อมูลจะไม่เกิดการเปลี่ยนแปลงและ rollback

#### Consistency

ข้อมูลต้องมีความสอดคล้องกันหลังเกิด transaction
เช่น

1.A มี 500 / B มี 700

2.transaction โอนเงินจาก A ไป B 300 เสร็จสมบูรณ์

3.เมื่อตรวจสอบเงินในบัญชี A ต้องมีเงิน 200 / B ต้องมีเงิน 1000

#### Isolation

จะไม่มีระบบอื่นรบกวนข้อมูลเมื่อกำลังทำธุรกรรมอยู่จนกว่า transaction จะถูก commit 

Isolation Level มีหลายระดับ

1.Read Uncommitted อนุญาตให้ Transaction มองเห็นข้อมูลที่ไม่สมบูรณ์หรือข้อมูลที่ยังไม่ถูก COMMIT

2.Read Committed อนุญาตให้ Transaction เห็นข้อมูลเฉพาะข้อมูลที่ได้รับการ COMMIT แล้วเท่านั้น

3.Repeatable Read อนุญาตให้ Transaction เห็นข้อมูลที่ได้รับการ COMMIT แล้วเท่านั้นและจะไม่เปลี่ยนแปลงค่าตั้งต้นของ Transaction นั้นจนกว่าจะ เกิด COMMIT ขึ้น

4.Serializable เป็น isolation ระดับสูงที่สุด อนุญาตให้ Transaction เกิดขึ้นเป็นลำดับต่อกันเท่านั้น หากมี transaction ที่สองเข้ามาจะถูกตีกลับทันที

#### Durability

หาก transaction ถูก commit แล้วจะคงอยู่ในดาต้าเบสเสมอ

ในกรณีที่ commit แล้วแต่ไฟดับทำให้ process ทำงานไม่สำเร็จสามารถทำ WAL (Write Ahead Log) เพื่อบันทึกข้อมูล transaction ลงใน disk เมื่อ databse server กลับมาทำงานสามารถทำงานต่อได้จากการดู WAL เทียบกับข้อมูลและแก้ไขข้อมูลให้ถูกต้องตาม transaction
