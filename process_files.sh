#!/bin/bash

# Настройки
SOURCE_DIR="/home/alina/1c_files/for_analysis"
DEST_DIR="/home/alina/1c_files/processed"
LOG_FILE="/home/alina/logs/file_processor.log"
APP_PATH="/home/alina/Загрузки/Diplom-main/Diplom"

# Создаем папки, если их нет
mkdir -p "$SOURCE_DIR" "$DEST_DIR" "$(dirname "$LOG_FILE")"

# Функция для обработки файла
process_file() {
    local filepath="$1"
    local filename=$(basename "$filepath")
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local temp_file="${filename%.*}_temp.${filename##*.}"
    
    echo "$(date): [НАЧАЛО] Обработка файла: $filename" >> "$LOG_FILE"
    echo "📄 Найден файл: $filename"
    
    echo "🔍 Запуск анализатора для: $filename"
    
     curl -X POST http://localhost:5000/api/analyze/file \
       -F "file=@$filepath" >> "$LOG_FILE" 2>&1
    
    ANALYZER_EXIT=$?
    
    if [ $ANALYZER_EXIT -eq 0 ]; then
        echo "✅ Анализатор завершил работу успешно" >> "$LOG_FILE"
        echo "✅ Анализ завершен для: $filename"
    else
        echo "❌ Ошибка анализатора (код: $ANALYZER_EXIT)" >> "$LOG_FILE"
        echo "❌ Ошибка при анализе: $filename"
    fi
    
    # Перемещаем файл в processed с префиксом даты
    local dest_path="$DEST_DIR/${timestamp}_${filename}"
    
    if mv "$filepath" "$dest_path"; then
        echo "$(date): [ГОТОВО] Файл перемещен: $filename -> ${timestamp}_${filename}" >> "$LOG_FILE"
        echo "📦 Файл перемещен в processed: ${timestamp}_${filename}"
    else
        echo "$(date): [ОШИБКА] Не удалось переместить $filename" >> "$LOG_FILE"
        echo "❌ Ошибка перемещения: $filename"
    fi
    
    echo "----------------------------------------" >> "$LOG_FILE"
}

# Экспорт функции для использования в подпроцессах
export -f process_file
export SOURCE_DIR DEST_DIR LOG_FILE APP_PATH

echo "$(date): ========== СКРИПТ ЗАПУЩЕН ==========" >> "$LOG_FILE"
echo "$(date): Мониторинг папки: $SOURCE_DIR" >> "$LOG_FILE"

# Обработка уже существующих файлов при запуске
for existing_file in "$SOURCE_DIR"/*; do
    if [ -f "$existing_file" ]; then
        echo "📁 Найден существующий файл: $(basename "$existing_file")"
        process_file "$existing_file"
    fi
done

# Основной цикл мониторинга
inotifywait -m "$SOURCE_DIR" -e create -e moved_to --format '%w%f' |
while read filepath; do
    # Небольшая задержка, чтобы убедиться, что файл полностью скопирован
    sleep 1
    
    # Проверяем, что файл существует и это не временный файл
    if [ -f "$filepath" ] && [[ ! "$filepath" =~ \.tmp$ ]] && [[ ! "$filepath" =~ \~$ ]]; then
        process_file "$filepath"
    fi
done
