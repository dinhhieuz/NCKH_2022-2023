package com.example.test4;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    Button btnDn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnDn = (Button)findViewById(R.id.buttonDn);

        btnDn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ac2 = new Intent (MainActivity.this, MainActivity2.class);
                startActivity(ac2);
            }
        });
    }
}