From Data Analyst to Data Engineer: My 12-Month Self-Study Roadmap
The exact tools I'm learning, the projects I'm building, and the mistakes I'm already expecting to make

Ibrahim Salami
May 16, 2026
10 min read
Share

Generated with Gemini AI
To be honest. A part of me started this journey because data engineering is one of the hottest and highest-paying careers right now. I’m not going to pretend that wasn’t a factor.

But there’s more to it than that.

I’ve been learning data analytics for a while now. SQL, Power BI, Python (Pandas, NumPy, a little Polars), data cleaning, EDA. You name it, I’ve been in the weeds with it. And I genuinely enjoy it. But somewhere along the way, I started getting curious about what happens before the data lands on my desk. How does it move? Who builds those pipelines? What does the infrastructure behind all of this actually look like?

That curiosity planted a seed.

Then AI started making a lot of what I do faster and easier. Which is great. But it also made me think: if AI can handle the analysis, what’s my edge? What can I build and understand that goes deeper? I work as an IT System Analyst at a startup, and while I enjoy the work, I realized I wasn’t challenging myself the way I wanted to. I was ready for more.

The final push came from a video by Data With Baraa, where he laid out a complete data engineering roadmap. Something about seeing it structured and broken down made it feel real and doable. So here I am.

I’m learning data engineering in public. And this article is the beginning of that journey.

Also, just leaving a disclaimer that I’m not affiliated with Data with Baraa. I’m just sharing my personal journey. Hope it helps.

Why Data Engineering Specifically
I want to spend a moment here because I think this question deserves a real answer.

Data analytics taught me how to work with data after it arrives. Clean it, explore it, visualize it, draw insights from it. That skillset is genuinely valuable. But the more I learned, the more I kept bumping into the same wall. The data I was working with had already been shaped and moved by someone else. Someone had built the pipeline that brought it to me. Someone had decided how it was stored, how it was structured, how often it refreshed.

I wanted to be that person.

Data engineering sits upstream from analytics. It’s about building the systems that make analysis possible in the first place. Data pipelines, storage architecture, workflow orchestration, large-scale data processing. These are the foundations everything else is built on. And honestly, that kind of infrastructure work appeals to me in a way that pure analysis no longer does.

There’s also a practical argument. Data engineering roles consistently rank among the highest paying in the data industry. As AI tools get better at automating the analytical layer, the demand for people who can build and maintain reliable data infrastructure is only going to grow. I’d rather be building the pipes than just using them.

And one more thing. The startup I work at doesn’t use any of the tools I’m about to learn. Which means every hour I put into this is entirely self-directed. No team to learn from, no work projects to apply it on. Just me, the internet, and whatever I can build on my own. That’s a challenge I’m choosing on purpose.

Why I’m Doing This in Public
Writing about what I learn is something I already believe in deeply. It forces you to actually understand something before you explain it. It keeps you accountable. And over time, it builds something that a resume alone never could.

But I’ll be honest about my fears too, because I think that’s the point of doing this publicly.

I have shiny object syndrome. There, I said it. I’ve explored graphic design, animation, writing, marketing, and IT before landing in data. There’s always something new and exciting pulling my attention. Data engineering could easily get replaced by the next flashy thing in my feed if I’m not intentional about it.

Consistency is another one. I work a 9-5 where I barely touch the tools I’ll be learning. There’s no natural reinforcement at work, no colleague I can bounce Airflow questions off of. I’m building this entirely on my own time, outside of my job responsibilities.

And balance. Three to four hours a day is the goal. Some days that will feel easy. Other days it will feel impossible.

Publishing this journey is my accountability system. If I go quiet, you’ll know I slipped. And I’d rather not slip.

What I’m Starting With
I’m not starting from zero, which helps. I already have beginner to intermediate SQL knowledge from my data analytics work, basic Python fundamentals, and some hands-on experience with Pandas. That gives me a foundation to build on rather than rebuild from scratch.

Here’s the full learning stack, roughly in the order I’ll be tackling it.

1. SQL: Going Deeper Than Analytics
I know SQL. But analytics SQL and engineering SQL are different animals. I’ll be going deeper into query optimization, indexing, working with very large datasets, and writing SQL that’s built for performance rather than just exploration. If you’ve only ever used SQL to pull and filter data, there’s a whole other layer underneath worth understanding.

Why it’s first: Everything in data engineering eventually touches SQL. Getting sharp here before layering in more complex tools makes the rest of the journey easier.

2. Python: From Exploratory to Production-Ready
I have the basics. Pandas, NumPy, some Polars. But the Python I’ve been writing lives mostly in notebooks. Exploratory, messy, not built to last. The goal now is to write cleaner, more structured, reusable code. Functions, modules, error handling, scripting. The kind of Python you’d actually put in a pipeline.

Why it matters: Python is the glue that holds most modern data engineering stacks together. Airflow uses it. PySpark is built on it. Getting comfortable here is non-negotiable.

3. Git and GitHub: Version Control Done Properly
I’ll be honest. My Git knowledge is currently “copy the command, hope it works.” That has to change. Version control is fundamental to working like an engineer rather than just an analyst. I’ll be learning branching, pull requests, and how to manage code properly across projects.

Why it matters: Every project I build from here on goes on GitHub. It’s portfolio, it’s discipline, and it’s how real teams work.

4. Apache Spark and PySpark: Big Data Processing
This is where things get genuinely exciting. Apache Spark is one of the most widely used engines for processing large-scale data. PySpark is the Python API for it, which means I can use a language I’m already somewhat familiar with to work with distributed data at scale.

The jump from Pandas to Spark is a mindset shift. Pandas works on a single machine. Spark is built to run across clusters. Learning to think in that distributed way is one of the skills that separates data engineers from analysts.

Why it matters: If you want to work with big data in a production environment, Spark is almost unavoidable. It shows up in job descriptions constantly and is core to the Databricks ecosystem I’ll be building toward.

5. Apache Airflow: Orchestrating Data Pipelines
Data pipelines don’t run themselves. You need something to schedule them, monitor them, and handle failures gracefully. That’s where workflow orchestration tools come in, and Airflow is my pick.

I considered a few options here. Databricks Workflows is great if you’re already deep in the Databricks ecosystem. Azure Data Factory makes sense for Azure-heavy environments. But Airflow is free, open-source, cloud-agnostic, and widely used across the industry. It also teaches you the core concepts of orchestration in a way that transfers to other tools. Starting with Airflow felt like the right call, especially since I’m trying to keep costs low.

Why it matters: Orchestration is what turns a collection of scripts into an actual pipeline. Understanding Airflow is understanding how production data workflows are managed.

6. Databricks: The Data Platform
At some point you need to pick a data platform and go deep on it. I’m going with Databricks. It’s built on top of Spark, it’s in high demand, and it has a free Community Edition that lets you practice without paying for cloud credits.

The alternatives are solid too. Snowflake is a clean, fast SQL warehouse that a lot of companies love. BigQuery is Google’s fully managed, serverless option and genuinely excellent if you’re leaning toward Google Cloud. But Databricks sits at the intersection of big data, machine learning, and data engineering in a way that matches where I want to go. It made the most sense for my goals.

Why it matters: Employers want you to have platform experience. Going deep on one is more valuable than knowing a little about all of them.

How I’m Structuring the 12 Months
The honest answer is that this might take longer than 12 months. And I’m okay with that. I’d rather take 15 months and actually understand what I’m doing than rush through in 12 and come out shaky on the fundamentals.

The general approach is to move through each skill in order and not advance until I’ve built something with what I just learned. Tutorials are fine for orientation but projects are where real learning happens. My plan is to document each phase here on Towards Data Science: the concepts, the projects, the frustrations, and the wins.

For tracking progress, I’m using the Notion roadmap from Data With Baraa as my backbone. It breaks down each skill into core topics and lets me track where I am without getting overwhelmed by the full picture all at once.

As for time commitment, three to four hours a day is the target. Some of that will be structured learning. Some will be building. Some will be writing about what I just learned, which is its own form of studying.

What Success Looks Like
Landing a high-paying data engineering role is the goal. That’s real and I’m not going to dress it up.

But alongside that, I want to become a credible voice in this space. Someone who builds things worth talking about, documents the journey without filtering out the hard parts, and maybe makes the path a little clearer for someone coming up behind me.

The writing and the learning feed each other. The portfolio becomes the proof. The proof builds the brand. That’s the vision.

Starting Today
This article is my official start date. I’m not waiting until I feel ready or until everything is perfectly planned. I’m starting now, writing as I go, and letting the process be public and a little messy.

If you’re somewhere on a similar path. Whether you’re in analytics thinking about engineering, in IT wondering what’s next, or just someone trying to build skills that hold their value in an AI-accelerated world. Follow along.

I think we’ll have a lot to talk about. I’ll also be sharing my learnings on my YouTube channel. So feel free to subscribe below and follow along.

This is the first article in an ongoing series documenting my data engineering journey. I’ll be publishing regularly on my progress, the projects I’m building, and everything I learn along the way.

And if you want to get access to the Notion template, in case you’re on the same journey as I am, you can access it here.

Follow along on my journey below.

YouTube

Medium

LinkedIn

Twitter