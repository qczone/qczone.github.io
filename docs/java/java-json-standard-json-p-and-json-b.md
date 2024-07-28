# Java 的 JSON 规范：JSON-P 和 JSON-B

JSON 大家都不陌生，Jackson、Gson 和 Fastjson 大家也都不陌生，都是常用的 JSON 库。今天想聊点大家可能陌生的，那就是 Java 的 JSON 规范。

Java 的 JSON 规范分成两个，JSON-P 和 JSON-B，下面给大家详细介绍一下这两个。

## JSON-P（Java API for JSON Processing）

> [The Java Community Process(SM) Program - JSRs: Java Specification Requests - detail JSR# 353 (jcp.org)](https://www.jcp.org/en/jsr/detail?id=353)

JCP 官网是这样描述的：Java API for JSON Processing (JSON-P) JSR 将开发一个 Java API 来处理（如解析、生成、转换和查询）JSON。

简单来说就是 JSR 提供了一个 API，用来处理 JSON 数据，这个 API 的源码在 https://github.com/jakartaee/jsonp-api

使用的话需要在 pom.xml 中引入

```xml
<!-- https://mvnrepository.com/artifact/jakarta.json/jakarta.json-api -->
<dependency>
    <groupId>jakarta.json</groupId>
    <artifactId>jakarta.json-api</artifactId>
    <version>2.1.3</version>
</dependency>
```

但是，想使用的话引入这个可不够，因为它只是 API，需要有实现类才行，官方的默认实现是 eclipse 的 passon源码地址是[eclipse-ee4j/parsson: Parsson Project (github.com)](https://github.com/eclipse-ee4j/parsson)

使用的话需要在 pom.xml 中引入

```xml
<!-- https://mvnrepository.com/artifact/org.eclipse.parsson/parsson -->
<dependency>
    <groupId>org.eclipse.parsson</groupId>
    <artifactId>parsson</artifactId>
    <version>1.1.6</version>
</dependency>
```

未完待续