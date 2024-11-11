# 必要なコンポーネントを指定
idf_component_register(
    SRCS "main.c" 
         "sdcard_logger.c"
    INCLUDE_DIRS "."
)
