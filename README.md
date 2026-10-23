<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0d1117,50:3a0ca3,100:7209b7&height=260&section=header&text=KHALED&fontSize=90&fontColor=ffffff&animation=twinkling&desc=backend%20engineer%20%E2%80%A2%20distributed%20systems&descSize=18&descAlignY=72&fontAlignY=40&stroke=b5179e&strokeWidth=2" width="100%"/>

<h1 align="center">Hi, I'm Khaled <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="32"/></h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=900&color=F72585&center=true&vCenter=true&width=650&lines=%3E+building+systems+that+refuse+to+die;%3E+retries.+idempotency.+transactions.;%3E+kill+the+worker.+nothing+gets+lost.;%3E+charge+twice%3F+not+on+my+ledger." />
</p>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"/>

## ⚡ About me

<img align="right" src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="320"/>

- 🧠 **Backend engineer** who cares what happens when things go wrong
- 🔁 Into **idempotency, retries, queues, transactions** and crash recovery
- 🐹 Writing **Go** for concurrency, **Python/Django** for APIs, **Node.js** for pipelines
- 💸 Built a billing API that **never double-charges**
- 📦 Built an import pipeline that eats **500k rows** with flat memory
- 📡 Built an uptime monitor where **one hung endpoint can't stall the rest**
- 🌱 Currently going deeper into **distributed systems**

<br clear="right"/>

```console
khaled@prod:~$ kill -9 $(pgrep import-worker)
worker died mid-import
resuming from checkpoint... ✔ 500,000 rows · 0 lost · 0 duplicated

khaled@prod:~$ curl -X POST /pay -H "Idempotency-Key: 42"  # x8 threads
✔ charged once

khaled@prod:~$ ./probe --target=hung-endpoint.com
✔ other monitors unaffected. it's fine. everything is fine.
```

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"/>

## 🛠️ Tech stack

<details open>
<summary><b>⚙️ Backend</b></summary>
<br/>

![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white)
![Gin](https://img.shields.io/badge/Gin-008ECF?style=for-the-badge&logo=go&logoColor=white)
</details>

<details open>
<summary><b>🗄️ Data & Queues</b></summary>
<br/>

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)
</details>

<details open>
<summary><b>🐳 DevOps & Tools</b></summary>
<br/>

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
</details>

<details>
<summary><b>🎨 Frontend (when I have to)</b></summary>
<br/>

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socketdotio&logoColor=white)
</details>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"/>

## 📊 Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=SupeeerMario&show_icons=true&theme=tokyonight&hide_border=true&hide=stars&count_private=true" height="170"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=SupeeerMario&layout=compact&theme=tokyonight&hide_border=true" height="170"/>
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=SupeeerMario&theme=tokyonight&hide_border=true" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/SupeeerMario/SupeeerMario/output/github-snake-dark.svg" />
    <img src="https://raw.githubusercontent.com/SupeeerMario/SupeeerMario/output/github-snake.svg" alt="snake eating my contributions" />
  </picture>
</p>

## 📫 Connect

<p align="left">
  <a href="https://github.com/SupeeerMario"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
  <!-- TODO: put your real links in and uncomment
  <a href="https://linkedin.com/in/YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:YOUR-EMAIL"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  -->
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7209b7,50:3a0ca3,100:0d1117&height=120&section=footer" width="100%"/>
