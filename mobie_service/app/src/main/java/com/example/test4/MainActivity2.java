package com.example.test4;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

public class MainActivity2 extends AppCompatActivity {

    Spinner spinner1, spinner2, spinner3, spinner4;
    Button btnOK;



    String[] ngchamthi = {"1-1-2023","2-1-2023","3-1-2023","4-1-2023","5-1-2023"};
    String[] monthi = {"Cơ sở lập trình","Cơ sở dữ liệu","Mạng và truyền thông","Phân tích thiết kế HTTT"};
    String[] cathi = {"0700_0830","0900_1030","1330_1500","1530_1700"};
    String[] phongthi = {"D001","D002","D003","D004"};

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        spinner1=findViewById(R.id.ngchamthi);
        spinner2=findViewById(R.id.monthi);
        spinner3=findViewById(R.id.cathi);
        spinner4=findViewById(R.id.phongthi);
        btnOK = findViewById(R.id.ok);

        ArrayAdapter<String> adapter1=new ArrayAdapter<String>(MainActivity2.this,android.R.layout.simple_spinner_item,ngchamthi);
        ArrayAdapter<String> adapter2=new ArrayAdapter<String>(MainActivity2.this,android.R.layout.simple_spinner_item,monthi);
        ArrayAdapter<String> adapter3=new ArrayAdapter<String>(MainActivity2.this,android.R.layout.simple_spinner_item,cathi);
        ArrayAdapter<String> adapter4=new ArrayAdapter<String>(MainActivity2.this,android.R.layout.simple_spinner_item,phongthi);

        adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        adapter3.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        adapter4.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spinner1.setAdapter(adapter1);
        spinner2.setAdapter(adapter2);
        spinner3.setAdapter(adapter3);
        spinner4.setAdapter(adapter4);


        spinner1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String value=spinner1.getItemAtPosition(i).toString();

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinner2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String value=spinner2.getItemAtPosition(i).toString();

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinner3.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String value=spinner1.getItemAtPosition(i).toString();

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinner4.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                String value=spinner1.getItemAtPosition(i).toString();

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });
        btnOK.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ac2 = new Intent (MainActivity2.this, MainActivity3.class);
                startActivity(ac2);
            }
        });

    }

}