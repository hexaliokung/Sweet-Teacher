pg.sprite.Group()
    คือคลาสใน Pygame ที่ใช้สำหรับรวบรวมสไปร์ทหลายๆ ตัวเข้าด้วยกัน ซึ่งช่วยให้การอัปเดตและการวาดภาพทำได้ง่ายขึ้น
โดยคุณสามารถเรียกใช้คำสั่ง update() และ draw() กับกลุ่มนี้เพียงครั้งเดียวเพื่อจัดการทุกสไปร์ทที่อยู่ในกลุ่ม


self.clock = pg.time.Clock()
    คือการสร้างอ็อบเจกต์ Clock จากโมดูล pygame ซึ่งใช้สำหรับการควบคุมอัตราเฟรมเรต (frame rate) ของเกม
โดยจะเก็บเวลาและช่วยในการคำนวณความเร็วของเฟรม เพื่อให้เกมสามารถทำงานได้ตามอัตราเฟรมที่กำหนด
    ดังนั้น ถ้าจะแปลในบริบทของโค้ดเป็นภาษาไทย อาจแปลได้ว่า:
self.clock เป็นตัวจับเวลา (Clock) ที่ใช้สำหรับควบคุมความเร็วในการอัปเดตและการแสดงผลของเกม


pg.key.set_repeat(500, 100)
    ใน Pygame ใช้สำหรับการตั้งค่าการทำซ้ำของการกดปุ่มคีย์บอร์ด เมื่อผู้ใช้กดปุ่มค้างไว้
โปรแกรมจะรับรู้ว่าปุ่มถูกกดซ้ำตามช่วงเวลาที่กำหนด

รายละเอียดของคำสั่งนี้:
- 500 (มิลลิวินาที) คือเวลาที่จะรอก่อนที่จะเริ่มตรวจจับการกดปุ่มซ้ำครั้งแรกหลังจากที่ผู้ใช้กดปุ่มค้างไว้
- 100 (มิลลิวินาที) คือช่วงเวลาหลังจากนั้นที่ปุ่มจะถูกตรวจจับว่าถูกกดซ้ำเรื่อยๆ ในทุกๆ 100 มิลลิวินาที
    ตราบเท่าที่ผู้ใช้ยังคงกดปุ่มค้างไว้

