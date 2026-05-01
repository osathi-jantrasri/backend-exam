## Question
![](/assets/q_indexing.png)
## Response Section

#### ข้อดี 

- หาข้อมูลได้เร็ว (SELECT) 
- รวมถึงกาเรียงข้อมูลด้วย (ORDER BY, GROUP BY, DISTINCT)

#### ข้อเสีย

- กินพี้นที่
- ทำให้เขียนข้อมูลได้ช้าลง (INSERT, UPDATE, DELETE) เพราะต้องสร้าง Index ใหม่เรื่อยๆ

#### ข้อจำกัด

- ทำ Indexing กับ column ได้จำกัดควรทำกับ column ที่ใช้บ่อยๆเท่านั้น WHERE, JOIN, GROUP BY, ORDER BY, DISTINCT บ่อยๆ

- ทำ Indexing กับ column ที่เป็นข้อมูลขนาดใหญ่เช่น ภาพ หรือ ข้อความยาวๆ ไม่ได้

- ไม่ควรทำกับ column ที่ Low cardinality เช่น TRUE/FALSE

- ทำให้การเขียนข้อมูลช้า เพราะต้องทำ indexing ด้วย เกิดปัญหาการ lock เป็นเวลานาน

- ข้อมูลที่มีการเขียนตลอด เช่น logging, อุปกรณ์ IoT sensor ไม่เหมาะกับการทำ indexing

