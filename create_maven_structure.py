import os

def create_spring_boot_structure(project_name):
    # Define the basic structure of the project
    structure = {
        project_name: [
            "src/main/java/com/example/demo",  # Adjust package structure as needed
            "src/main/resources",
            "src/test/java/com/example/demo",
            "src/test/resources",
            "target",  # Compiled code goes here
            ".gitignore",
            "pom.xml",
            "README.md",
            "mise.toml",  # Added mise.toml to the structure
        ]
    }

    # Create the directories and files
    for folder, subfolders in structure.items():
        os.makedirs(folder, exist_ok=True)  # Create the main project directory
        for item in subfolders:
            path = os.path.join(folder, item)
            if item.startswith("src/main/java"):
                os.makedirs(path, exist_ok=True)  # Create Java package structure
                # Create a sample Java class in the main package
                with open(os.path.join(path, "DemoApplication.java"), "w") as f:
                    f.write(
                        "package com.example.demo;\n\n"
                        "import org.springframework.boot.SpringApplication;\n"
                        "import org.springframework.boot.autoconfigure.SpringBootApplication;\n\n"
                        "@SpringBootApplication\n"
                        "public class DemoApplication {\n"
                        "    public static void main(String[] args) {\n"
                        "        SpringApplication.run(DemoApplication.class, args);\n"
                        "    }\n"
                        "}\n"
                    )
            elif item.startswith("src/main/resources"):
                os.makedirs(path, exist_ok=True)  # Create resources directory
                # Create an application properties file
                with open(os.path.join(path, "application.properties"), "w") as f:
                    f.write("# Application properties go here\n")
            elif item.startswith("src/test/java"):
                os.makedirs(path, exist_ok=True)  # Create test package structure
                # Create a sample test class
                with open(os.path.join(path, "DemoApplicationTests.java"), "w") as f:
                    f.write(
                        "package com.example.demo;\n\n"
                        "import org.junit.jupiter.api.Test;\n"
                        "import org.springframework.boot.test.context.SpringBootTest;\n\n"
                        "@SpringBootTest\n"
                        "class DemoApplicationTests {\n"
                        "    @Test\n"
                        "    void contextLoads() {\n"
                        "    }\n"
                        "}\n"
                    )
            elif item == ".gitignore":
                with open(path, "w") as f:
                    f.write(
                        "/target/\n"
                        "*.class\n"
                        "*.jar\n"
                        "*.war\n"
                        "*.log\n"
                        "*.iml\n"
                        ".idea/\n"
                    )
            elif item == "pom.xml":
                with open(path, "w") as f:
                    f.write(
                        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                        "<project xmlns=\"http://maven.apache.org/POM/4.0.0\"\n"
                        "         xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n"
                        "         xsi:schemaLocation=\"http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd\">\n"
                        "    <modelVersion>4.0.0</modelVersion>\n\n"
                        "    <groupId>com.example</groupId>\n"
                        "    <artifactId>demo</artifactId>\n"
                        "    <version>0.0.1-SNAPSHOT</version>\n"
                        "    <packaging>jar</packaging>\n\n"
                        "    <name>Demo</name>\n"
                        "    <description>Demo project for Spring Boot</description>\n\n"
                        "    <properties>\n"
                        "        <java.version>17</java.version>\n"  # Java version
                        "        <spring-boot.version>3.2.6</spring-boot.version>\n"  # Spring Boot version
                        "    </properties>\n\n"
                        "    <dependencies>\n"
                        "        <dependency>\n"
                        "            <groupId>org.springframework.boot</groupId>\n"
                        "            <artifactId>spring-boot-starter</artifactId>\n"
                        "        </dependency>\n"
                        "        <dependency>\n"
                        "            <groupId>org.springframework.boot</groupId>\n"
                        "            <artifactId>spring-boot-starter-test</artifactId>\n"
                        "            <scope>test</scope>\n"
                        "        </dependency>\n"
                        "    </dependencies>\n\n"
                        "    <build>\n"
                        "        <plugins>\n"
                        "            <plugin>\n"
                        "                <groupId>org.springframework.boot</groupId>\n"
                        "                <artifactId>spring-boot-maven-plugin</artifactId>\n"
                        "                <version>${spring-boot.version}</version>\n"  # Reference the Spring Boot version here
                        "            </plugin>\n"
                        "        </plugins>\n"
                        "    </build>\n"
                        "</project>\n"
                    )
            elif item == "README.md":
                with open(path, "w") as f:
                    f.write("# " + project_name + "\n\n" "## Description\n\n")
            elif item == "mise.toml":  # Create the mise.toml file
                with open(path, "w") as f:
                    f.write(
                        "[plugins]\n"
                        "helm        = 'https://github.com/Antiarchitect/asdf-helm'\n"
                        "helmfile    = 'https://github.com/feniix/asdf-helmfile'\n"
                        "jib         = 'https://github.com/joschi/asdf-jib'\n"
                        "kubectl     = 'https://github.com/asdf-community/asdf-kubectl'\n"
                        "maven       = 'https://github.com/Proemion/asdf-maven'\n"
                        "pnpm        = 'https://github.com/jonathanmorley/asdf-pnpm'\n"
                        "kubelogin   = 'https://github.com/sechmann/asdf-kubelogin'\n"
                        "golang      = 'https://github.com/asdf-community/asdf-golang'\n"
                        "kuttl       = 'https://github.com/jimmidyson/asdf-kuttl'\n"
                        "crossplane  = 'https://github.com/BigGold1310/mise-crossplane-cli'\n\n"
                        "[tools]\n"
                        "helm        = '3.13.1'\n"
                        "helmfile    = '0.158.0'\n"
                        "java        = 'openjdk-17.0.2'\n"
                        "jib         = '0.12.0'\n"
                        "kubectl     = '1.29.3'\n"
                        "maven       = '3.9.5'\n"
                        "nodejs      = '18.18.2'\n"
                        "pnpm        = '8.10.0'\n"
                        "kubelogin   = '0.0.29'\n"
                        "golang      = '1.22.5'\n"
                        "kustomize   = '5.4.1'\n"
                        "crossplane  = '1.16.0'\n\n"
                        "#deactivated due to bug, switched temporarily to direct installation in CI/CD\n"
                        "#kuttl       = '0.15.0'\n\n"
                        "[settings]\n"
                        "experimental = true\n"
                        "jobs = 1\n\n"
                        "[tasks.pre]\n"
                        "description = 'Install dependencies'\n"
                        "run = \"\"\"\n"
                        "#!/usr/bin/env bash\n"
                        "\"\"\"\n\n"
                        "[tasks.post]\n"
                        "description = 'Install dependencies'\n"
                        "run = \"\"\"\n"
                        "#!/usr/bin/env bash\n"
                        "helm plugin install https://github.com/jkroepke/helm-secrets --version v3.13.0\n"
                        "helm plugin install https://github.com/chartmuseum/helm-push --version v0.10.3\n"
                        "helm plugin install https://github.com/databus23/helm-diff --version v3.6.0\n"
                        "\"\"\"\n"
                    )

    print(f"Project structure for '{project_name}' created successfully.")

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_spring_boot_structure(project_name)
