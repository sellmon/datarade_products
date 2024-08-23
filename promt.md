**С какого сайта дата-сет: Walmart**
Заполни шаблон документа в формате markdown на АНГЛИЙСКОМ ЯЗЫКЕ используя данные которые я предоставлю. Простым языком, 
который будет понятен разработчикам, аналитикам, менеджерам. Как будто ты говоришь с коллегой и объясняешь простым языком для чего 
это нужно и какие выгоды несет. Ты можешь дополнять, изменять их, чтобы они были более релевантны и отвечали задачи.

Задача: заполнить карточку дата-сета, который могут купить клиенты для тренировки своего ai-агента. Мы предоставляем 
данные для ai-агентов и бизнеса, который может использовать эти данные для аналитики, системы уведомлений, быстрого 
поиска данных для сотрудников, для повышения продаж и других кейсов. Мы можем взять данные с любого сайта, и 
адаптировать для ai-агентов, чтобы они могли использовать их вместе с ai-агентами.
Пример, если ты получаешь запрос на карточку для Amazon, ты готовишь эти данные именно в контексте Amazon. 
Учти, что не надо указывать данные, если они публично недоступны, так как мы можем брать только 
публичные данные.

Это осуществляется на платформе datarade.

Обязательные поля для заполнения:
- Заголовок (до 150 символов), пример: AI & ML Training Data | Artificial Intelligence (AI) | Machine Learning (ML) Datasets | Deep Learning Datasets | Easy to Integrate | Free Sample 
- Короткое Описание (до 300 символов), пример: APISCRAPY's AI & ML training data is meticulously curated and labelled to ensure the best quality. Our training data comes from a variety... 
- Описание (до 8000 символов): здесь можешь использовать данные которые я прислал, а также учесть контекст заголовка
- Категория данных дата-сета, 5 штук, пример: Natural Language Processing, (NLP) Data Annotated Imagery Data, 
  Machine Learning (ML), Data Synthetic Data, но лучше подойдет что-то в контексте агентов
- Размер компаний: укажи здесь 3 категории - малый, средний и большой
- Приведи примеры использования этих данных
- Объем данных: здесь мне нужно количество записей, которые мы можем предоставить, сделай оценку как разработчик, 
  сколько реально собрать данных с указанного ресурса за неделю, тут важна примерная цифра, так что не переживай об 
  оценке и не указывай слишком много
- Качество: оцени высоко
- Географическое покрытие: где в основном работает данная компания, если много рынков, то укажи просто континенты, 
  или регионы типа Африка, Европа простым списком
- Укажи атрибуты данных(название, тип, описание, пример, маппинг): эти поля указывают какие данные мы собираем, 
  подготовь примерный список (в одну строку) этих данных по данным атрибутам, пример: заголовок товара, текст, 
  заголовок товара на карточке товара, пример, (маппинг я не знаю что такое в данном контексте, если ты знаешь о маппинге на платформае 
  datarade, то добавь релевантный маппинг) 


Вот данные, которые я бы хотел чтобы ты учел:
1 - мы соберем данные для вас с указанных площадок (в разделе я укажу какие данные могут быть собраны)
2 - мы подготовим их для вашего ai мы сможем их доставить вам удобным способом через Rest-API, Websockets, tRPC/gRPC) 
и любые другие способы(там на датарейде это указывается в каждом объявлении)
Вы сможете получить обычные данные или в векторизированном формате
Вы сможете выбрать какой моделью создавать emdedding’и(LLama, ChatOPT, и другие … какие вы планируете или уже 
используете, мы предоставим данные как для локальных и так и для платных моделей)
Вы сможете выбрать базу данных откуда сможете получать векторные данные напрямую (Chroma, FAISS, QdrantVectorStore 
и другие)
3 - в итоге вы получите комбайн, который перерабатывает и выдает нужные вам данные с минимальными усилиями и 
адаптированными для ваших ai-нужд и/или других задач
4 - отдельный пункт, который может быть преимуществом, наш бизнес - это данные, но возможно будет полезным указать, 
что  мы сможем за отдельный прайс создать агента/встроить ai в ваш бизнес, и уже затем поставлять ему данные. Так 
как  для многих это будет гемор вкладываться в то, что они не понимают, и в теории это может быть барьером который  
многих отталкивает и мешает продажам. А также возможно имеет смысл уточнить, что бизнес сможет создать на основе  
этих данных аналитику/уведомления/… построенных на ai, так как скорее всего не C-level смотрит эти данные, а 
менеджеры,  разработчики, аналитики и они должны понимать как это работает/что подключение будет простым, что мы  
сделаем доп работу если необходимо


Вот готовый пример:
#### Ebay

### Title:  
AI & ML Training Data from eBay | Customizable for AI Agents | High-Quality eCommerce Dataset | Easy Integration

### Short Description:  
Our eBay dataset is tailored for AI and ML training, offering high-quality, structured data from one of the largest eCommerce platforms. Perfect for analytics, AI-driven notifications, and sales optimization, this dataset is easy to integrate with your AI models and databases.

### Description:  
The eBay dataset provides a comprehensive collection of eCommerce data, ideal for training AI models and enhancing various business operations. Our data is meticulously extracted and prepared for easy integration with your existing AI systems, allowing you to drive innovation and efficiency with minimal effort. Whether you are a small startup or a large enterprise, this dataset can be adapted to meet your specific needs.

Key features include:
- **Custom Delivery Options**: Receive data through Rest-API, Websockets, tRPC/gRPC, or other preferred methods.
- **Vectorized Data**: Choose from multiple embedding models (LLama, ChatGPT, etc.) and vector databases (Chroma, FAISS, QdrantVectorStore) for optimized performance.
- **Comprehensive Data Coverage**: Collecting data across multiple categories such as product listings, pricing trends, customer reviews, and seller ratings.
- **Ease of Integration**: Our data can be easily integrated into your existing AI systems, providing you with the flexibility to create AI-driven analytics, notifications, and other business applications with minimal hassle.
- **Additional Services**: Beyond data provision, we offer AI agent development and integration services, helping you seamlessly incorporate AI into your business processes.

With our dataset, you can enhance your sales strategies, improve customer service, and optimize operations using AI-powered insights. This dataset is ideal for training AI models that require high-quality, structured data, enabling businesses to stay ahead of the competition in the ever-evolving eCommerce landscape.

### Dataset Categories:  
- eCommerce Data
- Machine Learning (ML) Data
- AI Training Data
- Business Analytics Data
- Sales Optimization Data

### Company Size:  
- Small  
- Medium  
- Large

### Use Cases:  
1. **AI-Powered Search Optimization**: Enhance search capabilities on your eCommerce platform by training AI models to understand and predict user search behaviors.
2. **Dynamic Pricing Models**: Develop AI-driven pricing strategies that adjust in real-time based on market trends and competitor pricing.
3. **Customer Sentiment Analysis**: Use AI to analyze customer reviews and ratings, providing insights into product performance and customer satisfaction.
4. **Sales Forecasting**: Train AI models to predict future sales trends, enabling better inventory management and marketing strategies.
5. **AI-Driven Recommendations**: Create personalized product recommendation systems that increase customer engagement and sales.

### Data Volume:  
Estimated data volume: **100 million records** per week.

### Data Quality:  
High - Data is carefully extracted, cleaned, and formatted for optimal AI training performance.

### Geographic Coverage:  
- North America
- Europe
- Asia
- Australia

### Data Attributes:

| Attribute Name          | Type   | Description                                         | Example                       |
|-------------------------|--------|-----------------------------------------------------|-------------------------------|
| Product Title           | Text   | Title of the product as listed on eBay              | "Apple iPhone 13 Pro Max"     |
| Price                   | Float  | Current price of the product                        | "999.99"                      |
| Product Description     | Text   | Detailed description of the product                 | "New, unlocked, 128GB, Blue"  |
| Seller Rating           | Float  | Rating of the seller                                | "4.8"                         |
| Review Text             | Text   | Customer review text                                | "Excellent product, fast shipping!" |
| Listing Date            | Date   | Date when the product was listed                    | "2024-08-20"                  |
| Category                | Text   | Category under which the product is listed          | "Electronics"                 |
| Number of Bids          | Integer| Number of bids placed on an auction item            | "15"                          |
| Shipping Information    | Text   | Details about shipping options and costs            | "Free Shipping, 3-5 days"     |
| Seller Location         | Text   | Geographic location of the seller                   | "San Francisco, CA"           |

This dataset provides rich, structured data, ideal for businesses aiming to leverage AI for improved decision-making, customer engagement, and operational efficiency.