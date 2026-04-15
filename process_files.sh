#!/bin/bash

# ============================================
# ТРИ ПАПКИ
# ============================================
SOURCE_DIR="/home/alina/1c_files/for_analysis"
PROCESSED_DIR="/home/alina/1c_files/processed"
RESULT_DIR="/home/alina/1c_files/result"
LOG_FILE="/home/alina/logs/file_processor.log"

# Создаем папки
mkdir -p "$SOURCE_DIR" "$PROCESSED_DIR" "$RESULT_DIR" "$(dirname "$LOG_FILE")"

# Функция обработки файла
process_file() {
    local filepath="$1"
    local filename=$(basename "$filepath")
    local timestamp=$(date +"%Y%m%d_%H%M%S")
    local base_name="${filename%.*}"
    
    echo "$(date): [1] Обнаружен файл: $filename" >> "$LOG_FILE"
    echo "📄 Найден файл: $filename"
    
    # ============================================
    # ГЛАВНОЕ: ЗАПУСК АНАЛИЗАТОРА
    # ============================================
    echo "$(date): [2] Запуск анализатора для: $filename" >> "$LOG_FILE"
    echo "🔍 Запуск анализатора для: $filename"
    
    cd /home/alina/Загрузки/Diplom-main/Diplom
    python3 main.py "$filepath" "$RESULT_DIR" >> "$LOG_FILE" 2>&1
    
    ANALYZER_EXIT=$?
    echo "$(date): [3] Анализатор завершил с кодом: $ANALYZER_EXIT" >> "$LOG_FILE"
    
    if [ $ANALYZER_EXIT -eq 0 ]; then
        echo "$(date): [4] Анализ успешен" >> "$LOG_FILE"
        echo "✅ Анализ завершен для: $filename"
        
        # Перемещаем исходный файл в processed
        mv "$filepath" "$PROCESSED_DIR/${timestamp}_${filename}"
        echo "$(date): [5] Файл перемещен в processed: ${timestamp}_${filename}" >> "$LOG_FILE"
        echo "📦 Файл перемещен в processed"
    else
        echo "$(date): [ОШИБКА] Анализ не удался для: $filename" >> "$LOG_FILE"
        echo "❌ Ошибка анализа для: $filename"
    fi
    
    echo "----------------------------------------" >> "$LOG_FILE"
}

export -f process_file

echo "$(date): ========== ЗАПУСК МОНИТОРИНГА ==========" >> "$LOG_FILE"
echo "📁 Входная папка: $SOURCE_DIR"
echo "📁 Обработанные: $PROCESSED_DIR"
echo "📁 Результаты: $RESULT_DIR"

# Обработка существующих файлов
for existing_file in "$SOURCE_DIR"/*.bsl; do
    if [ -f "$existing_file" ]; then
        process_file "$existing_file"
    fi
done

# Мониторинг новых файлов
inotifywait -m "$SOURCE_DIR" -e create -e moved_to --format '%w%f' |
while read filepath; do
    sleep 1
    if [ -f "$filepath" ] && [[ "$filepath" == *.bsl ]]; then
        process_file "$filepath"
    fi
done
