# Java 的 JSON 规范：JSON-P 和 JSON-B

在现在的 Web 开发中，JSON 已成为数据交换的首选格式。 Java 开发者对 Jackson、Gson 和 Fastjson 等流行库已经很熟悉，但是其实除了这些，Java 平台还提供了自己的标准化 JSON 处理 API：JSON-P（Java API for JSON Processing）和 JSON-B（Java API for JSON Binding）。这两个规范分别针对不同的需求和场景，提供了处理 JSON 数据的标准方法。

## JSON-P（Java API for JSON Processing）

### 简介

JSON-P 是 Jakarta EE 的一部分，起初在 Java EE 7 中作为 JSR 353 引入，并在 Jakarta EE 8 中的 JSR 374 得到扩展。JSON-P 的主要目的是提供一个灵活的 API 来处理（解析、生成、转换和查询）JSON 数据。

### 核心功能

- **对象模型**：使用一组 Java 类以树状结构来映射 JSON 数据结构，方便操作复杂的 JSON 文档。
- **流模型**：通过事件驱动方式来处理 JSON 数据流，优化大型数据的处理。

### 依赖

要使用 JSON-P，需要在 pom.xml 中添加依赖
```xml
<!-- https://mvnrepository.com/artifact/jakarta.json/jakarta.json-api -->
<dependency>
    <groupId>jakarta.json</groupId>
    <artifactId>jakarta.json-api</artifactId>
    <version>2.1.3</version>
</dependency>
```

但这样是代码是跑不起来的，因为它只是 api，没有实现，需要选择一个实现，如 Eclipse Foundation 的 Parsson：

```xml
<!-- https://mvnrepository.com/artifact/org.eclipse.parsson/parsson -->
<dependency>
    <groupId>org.eclipse.parsson</groupId>
    <artifactId>parsson</artifactId>
    <version>1.1.7</version>
</dependency>
```

### 示例

**创建单个JSON对象和数组：**

```java
JsonObject person = Json.createObjectBuilder()
        .add("name", "iKun")
        .add("age", 30)
        .build();
System.out.println(person.toString());
// {"name":"iKun","age":30}

JsonArray people = Json.createArrayBuilder()
        .add(Json.createObjectBuilder().add("name", "iKun").add("age", 30))
        .add(Json.createObjectBuilder().add("name", "xhz").add("age", 25))
        .build();
System.out.println(people.toString());
// [{"name":"iKun","age":30},{"name":"xhz","age":25}]
```

**读取JSON数据：**

```java
String jsonData = "{\"name\":\"iKun\",\"age\":30}";
JsonReader reader = Json.createReader(new StringReader(jsonData));
JsonObject obj = reader.readObject();
reader.close();
System.out.println(obj);
// {"name":"iKun","age":30}
```

**遍历JSON数组：**

```java
String jsonArrayData = "[{\"name\":\"iKun\",\"age\":30},{\"name\":\"xhz\",\"age\":25}]";
JsonReader arrayReader = Json.createReader(new StringReader(jsonArrayData));
JsonArray array = arrayReader.readArray();
for (JsonObject person : array.getValuesAs(JsonObject.class)) {
    System.out.println(person.getString("name") + " is " + person.getInt("age") + " years old.");
}
arrayReader.close();
// iKun is 30 years old.
// xhz is 25 years old.
```

### 优缺点

**优点**：

- Jakarta EE 标准的一部分，简洁的 API，适合在 Jakarta EE 应用中使用。

**缺点**：

- 性能上不如 Jackson 和 Gson 等流行库。


## JSON-B（Java API for JSON Binding）

### 简介

JSON-B 是为了简化 Java 对象和 JSON 数据之间的转换而设计的规范，通过 JSR 367 作为 Jakarta EE 8 的一部分引入。它定义了一种标准的映射机制，同时允许通过注解自定义映射过程。

### 核心功能

- **自动映射**：简化 Java 对象到 JSON 的序列化和反序列化。
- **自定义映射**：通过注解调整映射行为，满足特定需求。

### 依赖

要使用 JSON-B，需要在 pom.xml 中添加依赖

```xml
<!-- https://mvnrepository.com/artifact/jakarta.json.bind/jakarta.json.bind-api -->
<dependency>
    <groupId>jakarta.json.bind</groupId>
    <artifactId>jakarta.json.bind-api</artifactId>
    <version>3.0.1</version>
</dependency>
```

和 JSON-P 一样，需要选择一个实现，如 Eclipse Foundation 的 Yasson：

```xml
<!-- https://mvnrepository.com/artifact/org.eclipse/yasson -->
<dependency>
    <groupId>org.eclipse</groupId>
    <artifactId>yasson</artifactId>
    <version>3.0.3</version>
    <scope>test</scope>
</dependency>
```

### 示例

```java
public class Person {
    public String name;
    public int age;

    // 构造函数、getter和setter省略
}

// 序列化
Person person = new Person();
person.name = "iKun";
person.age = 30;

Jsonb jsonb = JsonbBuilder.create();
String json = jsonb.toJson(person);
System.out.println(json);
// {"age":30,"name":"iKun"}

// 反序列化
Person personFromJson = jsonb.fromJson(json, Person.class);
System.out.println("Name: " + personFromJson.name);
// Name: iKun
```

### 优缺点

**优点**：

- 提供标准化的对象到 JSON 的转换。
- 可通过注解灵活定制映射，线程安全，实例可重用。

**缺点**：
- 依赖于 Jakarta EE 8+ 环境或相应的依赖库。

## 总结
尽管 JSON-P 和 JSON-B 不如 Jackson 和 Gson 那样广为人知，但作为 Java 的官方 JSON 处理规范，它们提供了标准化和集成化的解决方案。
