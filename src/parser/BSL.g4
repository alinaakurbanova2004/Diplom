grammar BSL;

// ============ ЛЕКСЕР (ТОКЕНЫ) ============

// Ключевые слова (в явном юникоде)
PEREM: '\u041F\u0435\u0440\u0435\u043C' ;                // Перем
EXPORT: '\u042D\u043A\u0441\u043F\u043E\u0440\u0442' ;    // Экспорт
PROCEDURE: '\u041F\u0440\u043E\u0446\u0435\u0434\u0443\u0440\u0430' ; // Процедура
END_PROCEDURE: '\u041A\u043E\u043D\u0435\u0446\u041F\u0440\u043E\u0446\u0435\u0434\u0443\u0440\u044B' ; // КонецПроцедуры
FUNCTION: '\u0424\u0443\u043D\u043A\u0446\u0438\u044F' ; // Функция
END_FUNCTION: '\u041A\u043E\u043D\u0435\u0446\u0424\u0443\u043D\u043A\u0446\u0438\u0438' ; // КонецФункции
IF: '\u0415\u0441\u043B\u0438' ;                          // Если
THEN: '\u0422\u043E\u0433\u0434\u0430' ;                  // Тогда
ELSE_IF: '\u0418\u043D\u0430\u0447\u0435\u0415\u0441\u043B\u0438' ; // ИначеЕсли
ELSE: '\u0418\u043D\u0430\u0447\u0435' ;                  // Иначе
END_IF: '\u041A\u043E\u043D\u0435\u0446\u0415\u0441\u043B\u0438' ; // КонецЕсли
FOR: '\u0414\u043B\u044F' ;                               // Для
TO: '\u041F\u043E' ;
WHILE: '\u041F\u043E\u043A\u0430' ;                       // Пока
LOOP: '\u0426\u0438\u043A\u043B' ;                        // Цикл
END_LOOP: '\u041A\u043E\u043D\u0435\u0446\u0426\u0438\u043A\u043B\u0430' ; // КонецЦикла
RETURN: '\u0412\u043E\u0437\u0432\u0440\u0430\u0442' ;    // Возврат
TRUE: '\u0418\u0441\u0442\u0438\u043D\u0430' ;            // Истина
FALSE: '\u041B\u043E\u0436\u044C' ;                       // Ложь
NULL: 'Null' ;                                            // NULL
UNDEFINED: 'Undefined' ;                                  // Неопределено
AND: '\u0418' ;                                           // И
OR: '\u0418\u041B\u0418' ;                                // ИЛИ
NOT: '\u041D\u0415' ;                                     // НЕ
// ДОБАВЛЯЕМ ТОКЕНЫ ДЛЯ ДИРЕКТИВ
DIRECTIVE_CLIENT: '&НаКлиенте' ;
DIRECTIVE_SERVER: '&НаСервере' ;
DIRECTIVE_CLIENT_SERVER: '&НаКлиентеНаСервере' ;

// Операторы
PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;
LESS: '<' ;
LESS_OR_EQUAL: '<=' ;
GREATER: '>' ;
GREATER_OR_EQUAL: '>=' ;
EQUAL: '=' ;
NOT_EQUAL: '<>' | '!=' ;

// Идентификаторы (русские и английские буквы)
ID: [a-zA-Z\u0410-\u044F\u0401\u0451_][a-zA-Z0-9\u0410-\u044F\u0401\u0451_]* ;


// Литералы
STRING: '"' ('""' | ~'"')* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

// Пробелы и комментарии
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;

// ============ ПАРСЕР (ПРАВИЛА) ============
bslFile: (variableDeclaration | localVariableDeclaration | procedure | function)* EOF;
// ПРАВИЛО ДЛЯ ДИРЕКТИВ
directive: DIRECTIVE_CLIENT | DIRECTIVE_SERVER | DIRECTIVE_CLIENT_SERVER ;

variableDeclaration: PEREM ID (EXPORT)? ';' ;
localVariableDeclaration: PEREM ID ';' ;

procedure: directive? PROCEDURE ID parameterList? statement* END_PROCEDURE ';'? ;
function: directive? FUNCTION ID parameterList? statement* END_FUNCTION ';'? ;

parameterList: '(' (parameter (',' parameter)*)? ')' ;
parameter: ('Знач')? ID ('=' expression)? ;

statement: assignment
         | ifStatement
         | forStatement
         | whileStatement
         | returnStatement
         | callStatement
         | localVariableDeclaration
         ;

assignment: ID '=' expression ';'? ;

ifStatement: IF expression THEN statement* (ELSE statement*)? END_IF ';'? ;

returnStatement: RETURN expression? ';'? ;

// Список аргументов для вызова принимает любые выражения
argumentList: expression (',' expression)* ;

// Вызов процедуры/функции
callStatement: ID '(' argumentList? ')' ';'? ;

// Выражения с приоритетами
expression: logicalOrExpression ;

// Цикл Для
forStatement: FOR ID '=' expression TO expression LOOP statement* END_LOOP ';'? ;

// Цикл Пока (если есть)
whileStatement: WHILE expression LOOP statement* END_LOOP ';'? ;

logicalOrExpression: logicalAndExpression (OR logicalAndExpression)* ;
logicalAndExpression: comparisonExpression (AND comparisonExpression)* ;

comparisonExpression: additiveExpression
    ( (LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL | EQUAL | NOT_EQUAL) additiveExpression )? ;

additiveExpression: multiplicativeExpression
    ( (PLUS | MINUS) multiplicativeExpression )* ;

multiplicativeExpression: unaryExpression
    ( (MULT | DIV) unaryExpression )* ;

unaryExpression: (PLUS | MINUS | NOT)? primaryExpression ;

primaryExpression: literal
                 | ID
                 | '(' expression ')'
                 | callStatement
                 ;

// Литералы
literal: STRING
       | NUMBER
       | TRUE
       | FALSE
       | NULL
       | UNDEFINED
       ;
                   
